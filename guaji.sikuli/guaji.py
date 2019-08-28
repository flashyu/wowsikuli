import time

import random

#第一步 1920*1080 缩放1
#第二步 设置英语打字
i = 0;
while True:
    
    if exists("1566911317174.png",0):
        doubleClick("1566911337994.png");
        time.sleep(20);

    elif exists("1566914662533.png",0):
        click(Location(10, 10));
        time.sleep(20);
    
    elif exists( "1566911490504.png"):
        doubleClick("1566911527418.png");
    #elif exists( "1566914519679.png",0):
    #    doubleClick("1566914526618.png");    
        time.sleep(20);
    elif exists("1566912124291.png",0):
        click("1566912173905.png");
        time.sleep(20);
    elif exists("1566912201827.png",0):
        click(Location(886, 567));
        time.sleep(1);
        click(Location(886, 567));
        time.sleep(1);
        type("账号");
        time.sleep(1);
        click(Location(884, 667));
        time.sleep(1);
        type("密码");
        time.sleep(1);
        click(Location(969, 760));
        time.sleep(10);
    else:
        time.sleep(random.randrange(40,80));
        print "我擦"
        click(Location(10, 10));
        time.sleep(1);
        if(i%2==0): 
            keyDown(Key.UP)
            time.sleep(0.5);
            keyUp(Key.UP)
        else:
            keyDown(Key.DOWN)
            time.sleep(0.5);
            keyUp(Key.DOWN)
        i=i+1;