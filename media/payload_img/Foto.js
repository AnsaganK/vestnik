function Foto(id, path) {
    Container.call(this, id);
    this.id = id;
    this.path = path
}

Foto.prototype = Object.create(Container.prototype);
Foto.prototype.constructor = Foto;

Foto.prototype.render = function () {


    let foto_list = $(".foto_list");

    let foto_list_item = $("<div />", {
        class: "foto_list_item"
    });

    let item_img = $("<img />", {
        class: "minimized",
        src: this.path,
        alt: "photo"
    });

    foto_list_item.append(item_img);
    foto_list.append(foto_list_item);



    $(function(){
        $('.minimized').click(function(event) {
            var i_path = $(this).attr('src');
            $('body').append('<div id="overlay"></div><div id="magnify"><img src="'+i_path+'"><div id="close-popup"><i></i></div></div>');
            $('#magnify').css({
                left: ($(document).width() - $('#magnify').outerWidth())/2,
                // top: ($(document).height() - $('#magnify').outerHeight())/2 upd: 24.10.2016
                top: ($(window).height() - $('#magnify').outerHeight())/2
            });
            $('#overlay, #magnify').fadeIn('fast');
            $('body').addClass("pop_overflow");
        });

        $('body').on('click', '#close-popup, #overlay', function(event) {
            event.preventDefault();

            $('#overlay, #magnify').fadeOut('fast', function() {
                $('#close-popup, #magnify, #overlay').remove();
            });
            $('body').removeClass("pop_overflow");

        });
    });
}
