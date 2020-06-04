import numpy as np
import pandas as pd
import tensorflow as tf
import mysql.connector, sys, tqdm, pickle, traceback, progressbar
import configparser as cfg
from os import environ
from sklearn import preprocessing
from os.path import exists
from os import makedirs
from scipy.io import mmread as load




def semauto(matrix, mask):




    # print(np.shape(mask))
    # print(np.shape(matrix))

    num_users= 1
    group_id = "POLIBA GROUP"
    with open('listaIDCAT.pkl', 'rb') as f:
        features = pickle.load(f)


    #
    # config_filename = sys.argv[1]
    #
    # config = cfg.ConfigParser()
    # config.read(config_filename)




    FLAGS = tf.app.flags.FLAGS
    tf.app.flags.DEFINE_integer('num_gpus', 1, "How many GPUs to use.")

    environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    k = 10

    epochs = 1000

    learning_rate = 0.3


    #config = tf.ConfigProto(allow_soft_placement=True)
    config = tf.ConfigProto(device_count={'GPU': 0})

    #with progressbar.ProgressBar(max_value=num_users) as bar:
    processed_user = 0
    for gpu in range(FLAGS.num_gpus):
        with tf.device('/cpu:0'):


            # with open(matrix_dir + '/{}/features'.format(users[user])) as f:
            #     features = list(f.read().splitlines())

            num_input = matrix.shape[1]  # num of items
            num_features = mask.shape[1]

            M = tf.placeholder(tf.float32, [None, num_features])

            X = tf.placeholder(tf.float32, [None, num_input])

            W1 = tf.get_variable("w1", shape=[num_input, num_features], dtype=tf.float32,
                                 initializer=tf.constant_initializer(0.01))

            hidden = tf.nn.sigmoid(tf.matmul(X, tf.multiply(W1, tf.cast(mask, dtype=tf.float32))))

            W2 = tf.get_variable("w2", shape=[num_features, num_input], dtype=tf.float32,
                                 initializer=tf.constant_initializer(0.01))

            output = tf.nn.sigmoid(tf.matmul(hidden, tf.multiply(W2, tf.cast(mask.T, dtype=tf.float32))))

            # Prediction

            y_pred = output

            # Targets are the input data.

            y_true = X

            loss = tf.losses.mean_squared_error(y_true, y_pred)

            grad_W1 = tf.gradients(loss, W1)[0]
            grad_W2 = tf.gradients(loss, W2)[0]

            new_W1 = W1.assign(tf.multiply(W1, M) - learning_rate * grad_W1)
            new_W2 = W2.assign(tf.multiply(W2, tf.transpose(M)) - learning_rate * grad_W2)

            extract_op = tf.matmul(X, W1)

            # Initialize the variables (i.e. assign their default value)
            init = tf.global_variables_initializer()

            with tf.Session(config=config) as session:
                session.run(init)

                l = 0.0
                for e in range(epochs):
                    _, _, l = session.run([new_W1, new_W2, loss], feed_dict={X: matrix, M: mask})
                print("Group: {} - Loss: {}".format(group_id, l))

                print("Group: {} - Extracting features".format(group_id))

                values = session.run(extract_op, feed_dict={X: matrix, M: mask})


                #print(np.shape(values))
                # check values rows!

                #faccio la media nel caso siano righe superiori a 1
                if(np.shape(values)[0]>1):
                    values = np.mean(values, axis=0)


                min_max_scaler = preprocessing.MinMaxScaler()
                values = values.reshape([-1, 1])
                # values = values.ravel()
                x_scaled = min_max_scaler.fit_transform(values)

                values = x_scaled.squeeze()

                up = {}


                for i, v in enumerate(values):
                    up[features[i]] = v

                print(up)

                s = [(k, up[k]) for k in sorted(up, key=up.get, reverse=True)]

                # with open("{}/{}.tsv".format(up_dir, users[user]), "w") as file:
                #     for k, v in s:
                #         file.write("{}\t{:.16f}\n".format(k, v))

                processed_user += 1
                #bar.update(processed_user)

            tf.reset_default_graph()
    return up

def createMask():
    db = mysql.connector.connect(user='mattarella', password='mattarella',
                                 host='127.0.0.1',
                                 database='dbaggregationstrategies')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    listaIDPOI = list()
    listaIDCAT = list()


    try:
        sql = """SELECT POI_ID, ID_category FROM ratings JOIN occurrences ON POI_ID = ID_POI WHERE group_ID = 5560054 """
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()

        for row in results:
            if(row[0] not in listaIDPOI):
                listaIDPOI.append(row[0])
            if(row[1] not in listaIDCAT):
                listaIDCAT.append(row[1])

        print('\n\n')

        with open('listaIDPOI.pkl', 'wb') as f1:
            pickle.dump(listaIDPOI, f1)
        f1.close()

        with open('listaIDCAT.pkl', 'wb') as f2:
            pickle.dump(listaIDCAT, f2)
        f2.close()

        mask = np.zeros((len(listaIDPOI), len(listaIDCAT)), dtype=np.float32)

        for row in results:
            mask[listaIDPOI.index(row[0])][listaIDCAT.index(row[1])] = 1


        np.save('mask.npy', mask)

        return mask



    except:
        traceback.print_exc()

def createMatrix(groupID):

    try:
        db = mysql.connector.connect(user='mattarella', password='mattarella',
                                     host='127.0.0.1',
                                     database='dbaggregationstrategies')


        with open('listaIDPOI.pkl', 'rb') as f:
            listIDPOI = pickle.load(f)

        cursor = db.cursor()


        sql = """ SELECT DISTINCT userID FROM ratings WHERE group_ID = %s"""
        cursor.execute(sql, (groupID,))
        results = cursor.fetchall()

        listIDUser = [e[0] for e in results]


        sql = """SELECT userID, POI_ID, rate FROM ratings WHERE group_ID = %s """
        cursor.execute(sql, (groupID,))
        results = cursor.fetchall()
        db.close()



        matrix = np.zeros((len(listIDUser), len(listIDPOI)), dtype=np.float32)

        for row in results:
            matrix[listIDUser.index(row[0])][listIDPOI.index(row[1])] = row[2]


    except:
        traceback.print_exc()


    min_max_scaler = preprocessing.MinMaxScaler()
    for i in range(len(matrix)):
        matrix[i] = min_max_scaler.fit_transform(matrix[i].reshape(-1, 1)).reshape(1, 10)

    return matrix

def createArray(groupID, userID):

    try:
        db = mysql.connector.connect(user='mattarella', password='mattarella',
                                     host='127.0.0.1',
                                     database='dbaggregationstrategies')


        with open('listaIDPOI.pkl', 'rb') as f:
            listIDPOI = pickle.load(f)

        cursor = db.cursor()



        sql = """SELECT POI_ID, rate FROM ratings WHERE group_ID = %s AND userID = %s """
        cursor.execute(sql, (groupID, userID))
        results = cursor.fetchall()
        db.close()



        matrix = np.zeros((1, len(listIDPOI)), dtype=np.float32)

        for row in results:
            matrix[0][listIDPOI.index(row[0])] = row[1]


    except:
        traceback.print_exc()


    min_max_scaler = preprocessing.MinMaxScaler()
    for i in range(len(matrix)):
        matrix[i] = min_max_scaler.fit_transform(matrix[i].reshape(-1, 1)).reshape(1, 10)

    return matrix



groupID = 5560054
userID= 172

mask = createMask()
matrix = createMatrix(groupID)
# matrix = createArray(groupID, userID)
semauto(matrix, mask)



