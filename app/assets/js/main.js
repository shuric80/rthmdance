$(document).ready(function(){
    // variables
    var $header_top = $('.header-top');
    var $nav = $('nav');
    // toggle menu 
    $header_top.find('a').on('click', function() {
        $(this).parent().toggleClass('open-menu');
    });
    // fullpage customization
    $('#fullpage').fullpage({
        sectionsColor: ['#B8AE9C', '#348899', '#F2AE72', '#5C832F'],
        sectionSelector: '.vertical-scrolling',
        slideSelector: '.horizontal-scrolling',
        navigation: true,
        slidesNavigation: true,
        css3: true,
        controlArrows: false,
        anchors: ['firstSection', 'secondSection', 'thirdSection', 'fourthSection'],
        menu: '#menu',

        afterLoad: function(anchorLink, index) {
            $header_top.css('background', 'rgba(0, 47, 77, .3)');
            $nav.css('background', 'rgba(0, 47, 77, .25)');
            if (index == 4) {
                $('#fp-nav').hide();
            }
        },

        onLeave: function(index, nextIndex, direction) {
            if(index == 4) {
                $('#fp-nav').show();
            }
        },

        afterSlideLoad: function( anchorLink, index, slideAnchor, slideIndex) {
            console.log('afterSlideLoad');
            console.log(anchorLink);
            console.log(slideIndex);
            if(anchorLink == 'secondSection' && slideIndex == 1) {
                
                $.fn.fullpage.setAllowScrolling(false, 'up');
                $(this).css('background', '#374140');
                $(this).find('h2').css('color', 'white');
                $(this).find('h3').css('color', 'white');
                $(this).find('p').css({
                    'color': '#DC3522',
                    'opacity': 1,
                    'transform': 'translateY(0)'
                });
            }
        },

        onSlideLeave: function( anchorLink, index, slideIndex, direction) {
            console.log('onSlideLeave');
            
        } 
    }); 
});
