/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
function main(){
    var xbx = 0;
    var xbs = 0;
    var pspro = 0;
    $('.consoles').hide();
    $('.xbonex-info').hide();
    $('.xbones-info').hide();
    $('.ps4-info').hide();
    $('.home').hide();
    $('.home').fadeIn(1000);
    $('.sub-cat').hide();
    $('.button').on('click', function() {
        $(this).next().slideToggle(400);
        $(this).toggleClass('active');
    });
    $('.console-button').on('click', function() {
        $('.home, #heading').fadeOut(1000);
        $('#heading').text('Consoles');
        $('#css').attr('href', 'consoles-style.css');
        $('.consoles, #heading').fadeIn(1000);
        $('.xbone-x').on('click', function() {
            $('.xbonex-info').slideToggle(400, function(){
                if (xbx % 2 === 0 || xbx === 0){
                    $('html').css('animation-name', 'xboxx-img');
                    $('#heading').css('color', 'whitesmoke');
                    xbx ++;
                } else if (xbx % 2 === 1) {
                    $('html').css('animation-name', 'background-xbx');
                    $('#heading').css('color', 'black');
                    xbx ++;
                };
            });
        });
        $('.xbone-s').on('click', function() {
            $('.xbones-info').slideToggle(400, function(){
                if (xbs % 2 === 0 || xbs === 0) {
                    $('html').css('animation-name', 'xboxs-img');
                    $('#heading').css('color', 'black');
                    xbs ++;
                } else if (xbs % 2 === 1) {
                    $('html').css('animation-name', 'background-xbs');
                    $('#heading').css('color', 'black');
                    xbs ++;
                };
            });
        });
        $('.ps4-pro').on('click', function() {
            $('.ps4-info').slideToggle(400, function() {
                if (pspro % 2 === 0 || pspro === 0) {
                    $('html').css('animation-name', 'ps4-img');
                    $('#heading').css('color', 'whitesmoke');
                    pspro ++;
                } else if (pspro % 2 === 1) {
                    $('html').css('animation-name', 'background-pspro');
                    $('#heading').css('color', 'black');
                    pspro ++;
                };
            });
        });
    });
}
$(document).ready(main);
