# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.


#these values stack with previous position for some reason. use hide and show again to gets basic values.
#image positions ajusted to hikaridefdef model. works best with vn sprites, as seen with seba
#positions for 2 characters on screen.
transform c1:
    xalign 0.5
    yalign -0.05
transform r2:
    xalign 0.7
    yalign -0.05
transform l2:
    xalign 0.2
    yalign -0.05
#postions for 4 characters on screen.
transform r4:
    xanchor 0.15
    yanchor -0.05
transform rc4:
    xanchor -0.7
    yanchor -0.05
transform lc4:
    xanchor -1.4
    yanchor -0.05
transform l4:
    xanchor -2.4
    yanchor -0.05
    
#sprites
#RESIZE ALL SPRITES TO 400x870
image sekaiegslide:
    "/sprite/sekaieg.png"
    zoom 1.5
    xalign 0.5 yalign 0.6
    linear 10 yalign 0.2
image sekaiegunslide:
    "/sprite/sekaieg.png"
    zoom 1.5 yalign 0.2
    linear 3 zoom 0.9
image cmatekun = "/sprite/cmatekun.png"
image hikaridef = "/sprite/hikaridef.png"
image hikaridefdefside:
    "/sprite/hikaridefdef.png" 
    xalign -1 yalign 0.02
    linear 0.8 xalign 0.1
image hikaridefjump:
    "/sprite/hikaridef.png"
    xalign 2.5 yalign 0.4 
    linear 0.1 xalign 0.5
image hikaridefdef = "/sprite/hikaridefdef.png"
image alberto:
    "/sprite/alberto.png"
    xalign 0.5 yalign 0.65
image hania = "/sprite/hania.png"
image ania = "/sprite/ania.png"
image hikaridefdeft:
    #im.MatrixColor(
    #"/spirte/hikaridefdef.png", im.matrix.opacity(0.0))
    "/sprite/hikaridefdef.png"
    zoom 0.5
    xalign 0.3 yalign 0.4
image bully1:
    "/sprite/bully.png"
    yalign 0.7
    zoom 1.3
image bully2:
    "/sprite/bully.png"
    zoom 1.7
    yalign 0.35
image edgybp:
    "/sprite/edgybp.png"
    zoom 1.7

#bcgs
image bcgklasawideroll:
    "/bcg/bcgklasawide.jpg"
    xalign 0.0 yalign 0.5
    linear 80.0 xalign 1.0 
image bcgklasafull = "/bcg/bcgklasafull.jpg"
image bcgfullroll:
    "/bcg/bcgfull.jpg"
    xalign 1.0 yalign 0.5
    linear 20.0 xalign 0.0
image bcg2sroll:
    "/bcg/bcg2.jpg"
    xalign 1.0 yalign 0.5
    linear 90 xalign 0.0
image black = "#000000"
image bedr:
    "/bcg/bedr.jpg"
    zoom 0.83
image hall:
    "/bcg/hall.jpg"
    zoom 0.32
image stairs:
    "/bcg/stairs.jpg"
    zoom 0.4
image tree:
    "/bcg/tree.jpg"
    zoom 0.6
image toile:
    "/bcg/toile.jpg"
    zoom 0.7

#music

#cgs
image gaypanic:
    "/cgs/gaypanic.jpg"
    zoom 1.3
    xalign 0.1
    yalign 0.35
    #pause 3
    #easein 0.2 xalign 0.85
image gaypanic2:
    "/cgs/gaypanic.jpg"
    zoom 1.3
    xalign 0.1
    yalign 0.35
    pause 3
    easein 0.2 xalign 0.85
image gaypanic3:
    "/cgs/gaypanic.jpg"
    zoom 1.3
    yalign 0.35
    xalign 0.85
    linear 0.7
    xalign 0.0
    yalign 0.7
    pause 0.4
    linear 1.0
    yalign 0.35
    xalign 0.85
    
#transformations
transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
        #yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
        xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:
        #yanchor 0.527 ypos 0.5
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

#Used when hiding sprites with dissolve to mirror the show effect
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:
        #yanchor 0.510 ypos 0.5
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300
