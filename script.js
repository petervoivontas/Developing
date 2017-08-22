/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
function main(){
    var xbx = 0;
    var xbs = 0;
    var ps4pro = 0;
    var ps4s = 0;
    var xbox_exp = 0;
    var ps4_exp = 0;
    var pages = 0;
    $('.consoles').hide();
    $('.pcs').hide();
    $('.parts').hide();
    $('.xbonex-info').hide();
    $('.xbones-info').hide();
    $('.ps4-info').hide();
    $('.ps4s-info').hide();
    $('.home').hide();
    $('.home').fadeIn(1000);
    $('.sub-cat').hide();
    $('.button').not($('.xbone > .button, .ps4 > .button')).on('click', function() {
        $(this).next().slideToggle(400);
    });
    $('.console-button').on('click', function() {
        $('.home, #heading').fadeOut(1000);
        $('#heading').text('Consoles');
        $('#css').attr('href', 'consoles-style.css');
        $('.consoles, #heading').fadeIn(1000);
        $('.xbone-x').on('click', function() {
            $('.xbonex-info').slideToggle(400, function(){
                if (xbx % 2 === 0 || xbx === 0){
                    $('html').css('animation-name', 'xbox');
                    xbx ++;
                } else if (xbx % 2 === 1) {
                    $('html').css('animation-name', 'xbox-reverse');
                    xbx ++;
                };
            });
        });
        $('.xbone-s').on('click', function() {
            $('.xbones-info').slideToggle(400, function(){
                if (xbs % 2 === 0 || xbs === 0) {
                    $('html').css('animation-name', 'xbox');
                    $('#heading').css('color', 'black');
                    xbs ++;
                } else if (xbs % 2 === 1) {
                    $('html').css('animation-name', 'xbox-reverse');
                    $('#heading').css('color', 'black');
                    xbs ++;
                };
            });
        });
        $('.ps4-pro').on('click', function() {
            $('.ps4-info').slideToggle(400, function() {
                if (ps4pro % 2 === 0 || ps4pro === 0) {
                    $('html').css('animation-name', 'ps4');
                    $('#heading').css('color', 'whitesmoke');
                    ps4pro ++;
                } else if (ps4pro % 2 === 1) {
                    $('html').css('animation-name', 'ps4-reverse');
                    $('#heading').css('color', 'black');
                    ps4pro ++;
                };
            });
        });
        $('.ps4s').on('click', function() {
            $('.ps4s-info').slideToggle(400, function() {
                if (ps4s % 2 === 0 || ps4s === 0) {
                    $('html').css('animation-name', 'ps4');
                    $('#heading').css('color', 'whitesmoke');
                    ps4s ++;
                } else if (ps4s % 2 === 1) {
                    $('html').css('animation-name', 'ps4-reverse');
                    $('html').css('color', 'black');
                    ps4s ++;
                    
                };
            });
        });
        $('.xbone > .button').on('click', function() {
            if (xbox_exp % 2 === 0 || xbox_exp === 0) {
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                xbox_exp ++;
            } else if (xbox_exp % 2 === 1 && ((xbx % 2 === 1 || xbs % 2 === 1) && (ps4pro % 2 === 1 || ps4s % 2 === 1))) {
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                if (xbx % 2 === 1 && (ps4pro % 2 === 1 || ps4s % 2 === 1)) {
                    var back1 = $('html').css('background-color');
                    $('html').css('background-color', back1);
                    $('.xbonex-info').slideToggle(400);
                    $('html').css('animation-name', 'xboxtops4');
                    xbx ++;
                };
                if (xbs % 2 === 1 && (ps4pro % 2 === 1 || ps4s % 2 === 1)) {
                    var back2 = $('html').css('background-color');
                    $('html').css('background-color', back2);
                    $('.xbones-info').slideToggle(400);
                    $('html').css('animation-name', 'xboxtops4');
                    xbs ++;
                };
            } else if (xbox_exp % 2 === 1 && xbx % 2 === 1) {
                $('.xbonex-info').slideToggle(400);
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                $('html').css('animation-name', 'xbox-reverse');
                xbox_exp ++;
                xbx ++;
            } else if (xbox_exp % 2 === 1 && xbs % 2 === 1) {
                $('.xbones-info').slideToggle(400);
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                $('html').css('animation-name', 'xbox-reverse');
                xbox_exp ++;
                xbs ++;
            } else {
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                xbox_exp ++;
            };
        });
        $('.ps4 > .button').on('click', function() {
            if (ps4_exp % 2 === 0 || ps4_exp === 0) {
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                ps4_exp ++;
            } else if (ps4_exp % 2 === 1 && ((xbx % 2 === 1 || xbs % 2 === 1) && (ps4pro % 2 === 1 || ps4s % 2 === 1))) {
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                if (ps4pro % 2 === 1 && (xbx % 2 === 1 || xbs % 2 === 1)) {
                    var back3 = $('html').css('background-color');
                    $('html').css('background-color', back3);
                    $('.ps4-info').slideToggle(400);
                    $('html').css('animation-name', 'ps4toxbox');
                    ps4pro ++;
                };
                if (ps4s % 2 === 1 && (xbx % 2 === 1 || xbs % 2 === 1)) {
                    var back4 = $('html').css('background-color');
                    $('html').css('background-color', back4);
                    $('.ps4s-info').slideToggle(400);
                    $('html').css('animation-name', 'ps4toxbox');
                    ps4s ++;
                };
            } else if (ps4_exp % 2 === 1 && ps4pro % 2 === 1) {
                $('.ps4-info').slideToggle(400);
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                $('html').css('animation-name', 'ps4-reverse');
                ps4_exp ++;
                ps4pro ++;
            } else if (ps4_exp % 2 === 1 && ps4s % 2 === 1) {
                $('.ps4s-info').slideToggle(400);
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                $('html').css('animation-name', 'ps4-reverse');
                ps4_exp ++;
                ps4s ++;
            } else {
                $(this).next().slideToggle(400);
                $(this).toggleClass('active');
                ps4_exp ++;
            };
        });
    });
    $('.pc-button').on('click', function() {
        $('.home, #heading').fadeOut(1000);
        $('#heading').text('Gaming PCs');
        $('#css').attr('href', 'pcs-style.css');
        $('.pcs, #heading').fadeIn(1000);
        $('.pages').on('click', function() {
            if (pages % 2 === 0) {
                $('.info').toggle('slide');
                $('.parts').delay(350).fadeIn(1000);
                $('.pages').text('Info');
                pages ++;
            } else if (pages % 2 === 1) {
                $('.parts').toggle('slide');
                $('.info').delay(350).fadeIn(1000);
                $('.pages').text('Parts');
                pages --;
            };
        });
    });
}
$(document).ready(main);
