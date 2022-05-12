screen interface_inventory():
    modal True
    zorder 100
    frame:
        #borders (1,1)
        #background "images/none.png"
        padding(4,4)
        xsize 1280 ysize 720

        imagebutton:
            align (.995, 0.01)
            idle "images/interface/close_screen_idle.png"
            hover "images/interface/close_screen_hover.png"
            action [Hide ("interface_inventory", transition=fade), Hide ("desc_show")]
        
        frame:
            xsize 700 ysize 200
            align (0.9, 0.9)

        frame:
            padding (3,3)
            xsize 700 ysize 300
            align (0.9, 0.5)
            
            vpgrid:
                scrollbars "vertical"
                mousewheel True
                cols 12
                spacing 5
                for item in pc.inventory:
                    imagebutton:
                        idle (imagefind(item[0], "idle"))
                        hover (imagefind(item[0], "hover"))
                        hovered [Show("desc_show", item=item[0], count=item[1])]
                        unhovered [Hide("desc_show")]
                        action [Call("useitem", item[0])] 



screen desc_show(item="", count=0):
    
    zorder 110
    frame:
        background "images/none.png"
        padding (0, 0)
        xsize 700 ysize 155
        align (0.9, 0.9)
        vbox:
            text "{b}" + items[item]["itemna"] + "{/b}" + ": " + str(count)
            text items[item]["desc"] align (0.5, 0)
    
        
    
init python:
    current_item = "None"
    selected_item = "None"
    text_desc = ""
    
    def itemfind(item):
        citem = items[item]["itemn"]
        return(citem)
    
    def descfind(item):           
        text_desc = items[item]["desc"]
        return(text_desc)
        
    
    def imagefind(item, status="idle"):
        if status == "idle":
            image=items[item]["img_i"]
        elif status == "hover":
            image=items[item]["img_h"]
        else:
            image = None
        return(image)
        
label useitem(item="None", how=1):
    $ pc.use_item(item, how)
    return

label useitem_cookie():
   $ pc.use_item("cookie")
   return
    