
// http://rateyo.fundoocode.ninja/

$(function () {

    $(".rateyo").rateYo({
        numStars: 10,
        spacing: "5px",
        fullStar: true,
        onSet: function (rating) {
            var rating = rating*2;
            $(this).parent().attr('value', rating.toString());

        }
    });
});
