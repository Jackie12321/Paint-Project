#By Jackie Li
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


col = 0
size = 10

redo = []
undo = []
touchedcanvas = 0

root = Tk()
root.withdraw()

once = True

font.init()
Font = font.SysFont("Comic Sans Font", 80)
title="Mario Paint"
txtpic = Font.render(title, True, (10,150,25))

screen = display.set_mode((1200,900))

#images for tools
marioimage = image.load("images/download.png")
pencilimage = image.load("images/Pencil.svg.png")
mariobg = image.load("images/mariobackground.png")
colour = image.load("images/colour.png")
goombaimage = image.load("images/download3.png")
daisyimage1 = image.load("images/daisy.png")
daisyimage = transform.scale(daisyimage1, (85,150))
luigiimage1 = image.load("images/luigi2.png")
luigiimage = transform.scale(luigiimage1, (100,155))
booimage1 = image.load("images/boo.png")
booimage = transform.scale(booimage1, (110,90))
starimage1 = image.load("images/star.png")
starimage = transform.scale(starimage1, (100,100))
eraserimage1 = image.load("images/eraser_1.png")
eraserimage = transform.scale(eraserimage1,(70,100))
brushimage1 = image.load("images/brush2.png")
brushimage = transform.scale(brushimage1,(340,200))
sprayimage1 = image.load("images/spray.png")
sprayimage = transform.scale(sprayimage1,(120,140))
clearimage1 = image.load("images/clear.png")
clearimage = transform.scale(clearimage1,(100,100))
fillimage1 = image.load("images/fill.png")
fillimage = transform.scale(fillimage1,(90,90))
saveimage1 = image.load("images/save.png")
saveimage = transform.scale(saveimage1,(50,50))
loadimage1 = image.load("images/load.png")
loadimage = transform.scale(loadimage1,(70,50))
lineimage1 = image.load("images/line.png")
lineimage = transform.scale(lineimage1,(100,100))
colimage1 = image.load("images/colpick.png")
colimage = transform.scale(colimage1,(100,100))
arrowimage1 = image.load("images/arrow.png")
arrowimage = transform.scale(arrowimage1,(100,35))
arrow2image1 = image.load("images/arrow2.png")
arrow2image = transform.scale(arrow2image1, (100,35))
circleimage1 = image.load("images/circle1.png")
circleimage = transform.scale(circleimage1, (100,100))
rectangleimage1 = image.load("images/rectangle.png")
rectangleimage = transform.scale(rectangleimage1,(500,440))

#variables for stamps and boxes
mariobg = screen.blit(mariobg, (-150,-350))
pencilRect = Rect(20,80,100,100)
eraserRect = Rect(140,80,100,100)
eraser = screen.blit(eraserimage,(150,80))
sprayRect = Rect(20,200,100,100)
spray = screen.blit(sprayimage,(18,185))
brushRect = Rect(140,200,100,100)
brush = screen.blit(brushimage,(115,180))
boxRect = Rect(140,320,100,100)
rectangle = screen.blit(rectangleimage,(10,200))
pencil = screen.blit(pencilimage,(20,80))
mario = screen.blit(marioimage,(250,750))
goomba = screen.blit(goombaimage,(400,750))
luigi = screen.blit(luigiimage,(520,745))
daisy = screen.blit(daisyimage,(650,750))
star = screen.blit(starimage,(870,750))
boo = screen.blit(booimage,(750,750))
lineRect = Rect(20,320,100,100)
line = screen.blit(lineimage,(20,320))
ovalRect = Rect(20,440,100,100)
oval = screen.blit(circleimage,(20,440))
undoRect = Rect(20,20,100,35)
undoarrow = screen.blit(arrowimage,(20,20))
redoRect = Rect(140,20,100,35)
redoarrow = screen.blit(arrow2image,(140,20))
saveRect = Rect(1050,125,50,50)
save1 = screen.blit(saveimage,(1050,125))
loadRect = Rect(1120,125,50,50)
load = screen.blit(loadimage,(1110,125))
colRect = Rect(140,440,100,100)
colpicker = screen.blit(colimage,(140,440))
clearRect = Rect(1062,200,100,100)
clear = screen.blit(clearimage,(1062,200))
fillRect = Rect(1062,320,100,100)
fill = screen.blit(fillimage,(1070,330))

canvasRect = Rect(265,80,750,650)

draw.rect(screen,(255,255,255),canvasRect)

tool = "pencil"
running = True
undo.append(screen.subsurface(canvasRect).copy())
while running:

    #title
    if once:
        screen.blit(txtpic, (500,20))
        once = False

    for e in event.get():
        if e.type == QUIT:
            running = False     

#from someone else
    #copying canvas for undo/redo
##        if e.type == MOUSEBUTTONDOWN and canvasRect.collidepoint(mx,my):    #mouse button and inside canvas
##            undo.append(screen.subsurface(canvasRect).copy())               #copies canvas into list
##            position += 1                                                   #adds 1 to position everytime to keep track of the images in the list
##            if position < len(undo) - 1:                                    #if position is less than second last item in list
##                while position != len(undo)-1:                              #keeps on deleting all images until length of list is equal to position
##                    undo.pop()                                              #remove last image in list

#got most of it online
    #flood fill
        if e.type == MOUSEBUTTONDOWN and canvasRect.collidepoint(mx,my) and tool == "fill":
            fx = mx                                                         #points for mouse position
            fy = my                                                         
            startcol = screen.get_at((fx,fy))                               #gets the colour of the point where the mouse is at
            fill_list = [(fx,fy)]                                           #list for the points that you need to check if they have been filled or not
            draw.line(screen,col,(fx,fy),(fx,fy))                           #draws a line on the first mouse position
            while len(fill_list) != 0:                                      #keeps on checking until the list is empty
                fx,fy = fill_list[0]                                        #gets the first x and y in the list
                
                if startcol == screen.get_at((fx,fy+1)):                    #checks if the colour of the bottom point is the same as the starting colour
                    draw.line(screen,col,(fx,fy+1),(fx,fy+1))               #draws a line at the bottom point
                    fill_list.append((fx,fy+1))                             #adds the bottom point into the list
                    
                if startcol == screen.get_at((fx+1,fy)):                    #checks if the colour of the right point is the same as the starting colour
                    draw.line(screen,col,(fx+1,fy),(fx+1,fy))
                    fill_list.append((fx+1,fy))
                    
                if startcol == screen.get_at((fx-1,fy)):                    #checks if the colour of the left point is the same as the starting colour
                    draw.line(screen,col,(fx-1,fy),(fx-1,fy))
                    fill_list.append((fx-1,fy))
                    
                if startcol == screen.get_at((fx,fy-1)):                    #checks if the colour of the top point is the same as the starting colour
                    draw.line(screen,col,(fx,fy-1),(fx,fy-1))
                    fill_list.append((fx,fy-1))
                
                del(fill_list[0])

    #clear
        if e.type == MOUSEBUTTONDOWN and clearRect.collidepoint(mx,my):              #copies canvas into list of images
                draw.rect(screen,(255,255,255),(265,80,750,650))
                undo.append(screen.subsurface(canvasRect).copy())
                redo = []

#someone elses                    
##    #clear
##        if e.type == MOUSEBUTTONDOWN and clearRect.collidepoint(mx,my):     
##            undo.append(screen.subsurface(canvasRect).copy())               #copies canvas into list of images
##            draw.rect(screen,(255,255,255),(265,80,750,650))
##            position += 1                                                   #adds 1 to position to keep track of list
##            draw.rect(screen,(255,255,255),(265,80,750,650))                #draws a white box over entire canvas
##            undo.append(screen.subsurface(canvasRect).copy())               
##            position += 1
##            if position < len(undo) - 1:                                    #if position less than length of second last item
##                while position != len(undo) and position != 0:              #if position does not equal to the length of the list, and position does not equal 0
##                    undo.pop()                                              #removes last item in list
                    
##    #undo/redo
##        if e.type == MOUSEBUTTONUP and undoRect.collidepoint(mx,my):
##            if position == len(undo):                                       #only copies when position is the last thing in undo list
##                undo.append(screen.subsurface(canvasRect).copy())
##            if position > 0:                                                #if position is greater than 0 then keep subtracting 1 from position
##                position -= 1
##            screen.blit(undo[position], (265,80))                           #blits previous image onto canvas
##
##        if e.type == MOUSEBUTTONUP and redoRect.collidepoint(mx,my):
##            if position == len(undo):                                       #only copies when position is the last thing in undo list/equal to length of list  
##                undo.append(screen.subsurface(canvasRect).copy())           #                                                                                  
##            if position < len(undo) - 1:                                    #if position is less than length of list then add 1                                ] when you click undo and draw something,
##                position += 1                                               #                                                                                  ] it will delee the following images in the list 
##            while position >= len(undo):                                    #if position is greater than or equal to length of list, keep subtracting 1        ] from your current position
##                position -= 1                                               #                                                                                  
##            screen.blit(undo[position], (265,80))                           #blits the following image

#gary's help
    #undo/redo
        if e.type == MOUSEBUTTONUP and touchedcanvas == 1:
                undo.append(screen.subsurface(canvasRect).copy())             #copies canvas and adds to list
                redo = []                                                     
                touchedcanvas = 0

        if e.type == MOUSEBUTTONUP and undoRect.collidepoint(mx,my):          
                if len(undo)>1:                                             
                    redo.append(undo[-1])
                    undo.pop()                                                #removes last item in undo list
                    screen.blit(undo[-1],(265,80))  
              
        if e.type == MOUSEBUTTONUP and redoRect.collidepoint(mx,my):
                if len(redo)>0:
                    screen.blit(redo[-1],(265,80))
                    undo.append(redo[-1])
                    redo.pop()
                    
                    
    #using scroll wheel for size                   
        if e.type == MOUSEBUTTONDOWN:                                       
            if e.button == 4:                                               #scroll wheel up    
                if size < 40:                                               #increases variable 'size' by 1 if size is less than 40
                    size += 1
                

            if e.button == 5:                                               #scroll wheel down
                if size > 10:                                               #decreases vairable 'size' by 1 if size is greater than 10
                    size -= 1

    #for stamp if using scroll wheel when placing a stamp it will not blit           
            if e.button != 4 and e.button != 5:
                px,py = mx,my                                               #variable for mouse position
                savE = screen.subsurface(canvasRect).copy()                 #variable to copy entire canvas

    #save file
        if e.type == MOUSEBUTTONDOWN and saveRect.collidepoint(mx,my):
            fileName = asksaveasfilename(parent=root,title="Save the image as . . . ") 
            if fileName != "":                                              #asks for a file name to save
                image.save(screen.subsurface(canvasRect),"%s.png"%(fileName))

    #load file
        if e.type == MOUSEBUTTONDOWN and loadRect.collidepoint(mx,my):
            fileLoad = askopenfilename(parent=root,title="Open Image:")     #asks to load a file
            if fileLoad != "":
                picture=image.load("%s" %(fileLoad))                        #allows user to be able to load png image
                screen.set_clip(canvasRect)
                screen.blit(picture,(265,80))                               #blits the loaded file on canvas
                screen.set_clip(None)

                
    #----------------------------------------------------------------
        mb = mouse.get_pressed()
        mx,my = mouse.get_pos()
        WHITE = (255,255,255)

        if mb[0]==1 and canvasRect.collidepoint(mx,my):
                touchedcanvas = 1
        if mb[2]==1 and canvasRect.collidepoint(mx,my):
                touchedcanvas = 1
        
    #colour wheel  
        if mb[0]==1 and colourpick.collidepoint(mx,my):
            col = screen.get_at((mx,my))                                    #gets colour from colour wheel only when left mouse button is pressedinside 'colourpick' box
            draw.rect(screen,col,(47,740,175,175))                          #draws the rectangle of the current colour where the mouse position is

        draw.rect(screen,col,(47,740,175,175))                              #displays current colour
        colourpick = screen.blit(colour,(60,750))                           #blits colour wheel image      
        
    #tool icons
        draw.rect(screen,(0,255,0),fillRect,2)
        draw.rect(screen,(0,255,0),clearRect,2)
        draw.rect(screen,(0,255,0),colRect,2)
        draw.rect(screen,(0,255,0),loadRect,2)
        draw.rect(screen,(0,255,0),saveRect,2)
        draw.rect(screen,(0,255,0),undoRect,2)
        draw.rect(screen,(0,255,0),redoRect,2)
        draw.rect(screen,(0,255,0),pencilRect,2)
        draw.rect(screen,(0,255,0),eraserRect,2)
        draw.rect(screen,(0,255,0),sprayRect,2)
        draw.rect(screen,(0,255,0),brushRect,2)
        draw.rect(screen,(0,255,0),lineRect,2)
        draw.rect(screen,(0,255,0),boxRect,2)
        draw.rect(screen,(0,255,0),ovalRect,2)

           
    #tools box(turns frame of box red when tool is selected)
        if mb[0]==1 and pencilRect.collidepoint(mx,my):                     #
            draw.rect(screen,(255,0,0),pencilRect,2)
            tool = "pencil"
            
        if mb[0]==1 and eraserRect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),eraserRect,2)
            tool = "eraser"
            
        if mb[0]==1 and sprayRect.collidepoint(mx,my):
            tool = "spray"
            draw.rect(screen,(255,0,0),sprayRect,2)
            
        if mb[0]==1 and brushRect.collidepoint(mx,my):
            tool = "brush"
            draw.rect(screen,(255,0,0),brushRect,2)

        if mb[0]==1 and mario.collidepoint(mx,my):
            tool = "mario"
            screen.blit(marioimage,(250,750))

        if mb[0]==1 and goomba.collidepoint(mx,my):
            tool = "goomba"
            screen.blit(goombaimage,(400,750))

        if mb[0]==1 and luigi.collidepoint(mx,my):
            tool = "luigi"
            screen.blit(luigiimage,(520,745))

        if mb[0]==1 and daisy.collidepoint(mx,my):
            tool = "daisy"
            screen.blit(daisyimage,(650,750))

        if mb[0]==1 and boo.collidepoint(mx,my):
            tool = "boo"
            screen.blit(booimage,(750,750))

        if mb[0]==1 and star.collidepoint(mx,my):
            tool = "star"
            screen.blit(starimage,(870,750))

        if mb[0]==1 and lineRect.collidepoint(mx,my):
            tool = "line"
            draw.rect(screen,(255,0,0),lineRect,2)

        if mb[0]==1 and boxRect.collidepoint(mx,my):
            tool = "box"
            draw.rect(screen,(255,0,0),boxRect,2)
            
        if mb[0]==1 and ovalRect.collidepoint(mx,my):
            tool = "oval"
            draw.rect(screen,(255,0,0),ovalRect,2)

        if mb[0]==1 and colRect.collidepoint(mx,my):
            tool = "pick"
            draw.rect(screen,(255,0,0),colRect,2)

        if mb[0]==1 and fillRect.collidepoint(mx,my):
            tool = "fill"
            draw.rect(screen,(255,0,0),fillRect,2)

        if mb[0]==1 and undoRect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),undoRect,2)

        if mb[0]==1 and redoRect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),redoRect,2)

        if mb[0]==1 and clearRect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),clearRect,2)

    #tools box2
        if tool == "pencil":
            draw.rect(screen,(255,0,0),pencilRect,2)
            
        if tool == "eraser":
            draw.rect(screen,(255,0,0),eraserRect,2)

        if tool == "spray":
            draw.rect(screen,(255,0,0),sprayRect,2)
            
        if tool == "brush":
            draw.rect(screen,(255,0,0),brushRect,2)

        if tool == "line":
            draw.rect(screen,(255,0,0),lineRect,2)

        if tool == "box":
            draw.rect(screen,(255,0,0),boxRect,2)
            
        if tool == "oval":
            draw.rect(screen,(255,0,0),ovalRect,2)

        if tool == "pick":
            draw.rect(screen,(255,0,0),colRect,2)

        if tool == "fill":
            draw.rect(screen,(255,0,0),fillRect,2)

    #pencil
        
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            if tool == "pencil":
                draw.line(screen,0,(omx,omy),(mx,my))                       #draws line at old x and y point and current mouse point

    #eraser            
            if tool == "eraser":                                            
                dx = mx - omx
                dy = my - omy
                dist=sqrt(dx**2+dy**2)
                for i in range(1,int(dist)):
                    coly=int(omy+i*dy/dist)
                    colx=int(omx+i*dx/dist)
                    draw.circle(screen,WHITE,(colx,coly),size)

                
    #spray
            if tool == "spray":
                for i in range(30):
                    sx=randint(-size,size)                                 #chooses random points between the size
                    sy=randint(-size,size)
                    if hypot(sx,sy)<size:                                  #only draws a circle when the hypotenuse of sx and sy is less than the size
                        draw.circle(screen,col,(mx+sx,my+sy),0)
    #brush              
            if tool == "brush":
                dx = mx - omx
                dy = my - omy
                dist=sqrt(dx**2+dy**2)                                    #distance formula to find hypotenuse of a triangle
                for i in range(1,int(dist)):                              #loops from 1 to the hypotenuse number
                    cy=int(omy+i*dy/dist)                                 #draws circles between mx,my and omx,omy 
                    cx=int(omx+i*dx/dist)
                    draw.circle(screen,col,(cx,cy),size)
                
    #mario stamp
            if tool == "mario":
                screen.blit(savE, (265,80))                               #copies canvas
                screen.blit(marioimage,(mx-55,my-75))                     #puts image where cursor is
                   
    #goomba stamp
            if tool == "goomba":
                screen.blit(savE, (265,80))
                screen.blit(goombaimage,(mx-55,my-75))

    #luigi stamp
            if tool == "luigi":
                screen.blit(savE, (265,80))
                screen.blit(luigiimage,(mx-55,my-75))
                
    #daisy stamp
            if tool == "daisy":
                screen.blit(savE, (265,80))
                screen.blit(daisyimage,(mx-35,my-75))
                
    #super star stamp
            if tool == "star":
                screen.blit(savE, (265,80))
                screen.blit(starimage,(mx-46,my-50))
                
    #boo stamp
            if tool == "boo":
                screen.blit(savE, (265,80))
                screen.blit(booimage,(mx-35,my-60))

    #line
            if tool == "line":
                screen.blit(savE, (265,80))                                 
                draw.line(screen, col, (px,py), (mx,my),size)
                
    #rectangle
            if tool == "box":
                screen.blit(savE, (265,80))
                rec = Rect(px,py,mx-px,my-py)
                draw.rect(screen,col, rec,size)
                
    #oval 
            if tool == "oval":
                screen.blit(savE, (265,80))
                rec = Rect(px,py,mx-px,my-py)
                rec.normalize()
                if size == abs(mx-px) and size == abs(my-py):
                    nothing = 0           
                if size > abs((mx-px)//2) or size > abs((my-py)//2):        #if the thickness of the ellipse is greater than the radius then draw a filled ellipse
                    draw.ellipse(screen, col,rec,0)
                if size < abs((mx-px)//2) and size < abs((my-py)//2):       #if the thickness of the ellipse is less than the radius then draw an unfilled ellipse       
                    draw.ellipse(screen,col,rec,size)

    #colour picker
            if tool == "pick":
                col=screen.get_at((mx,my))                                  #gets colour wherever you click on canvas
                draw.rect(screen, col,(47,740,175,175))                     #displays the colour

            screen.set_clip(None)

    #Filled shapes when you right click for box and oval/ellipse
        if mb[2]==1 and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)                                     #clips canvas so you can't draw outside
            if tool == "box":
                screen.blit(savE, (265,80))
                rec = Rect(px,py,mx-px,my-py)
                draw.rect(screen, col, rec,0)                               #draws a filled rectangle
                
            if tool == "oval":
                screen.blit(savE,(265,80))
                rec = Rect(px,py,mx-px,my-py)
                rec.normalize()
                draw.ellipse(screen,col,rec,0)                              #draws a filled ellipse
            screen.set_clip(None)

            
    #----------------------------------------------------------------
        omx,omy = mx,my
    display.flip()
    
font.quit()
del Font
quit()
