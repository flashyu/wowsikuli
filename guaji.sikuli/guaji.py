def gameStart():
    print 'game start';
    click("1574096724785.png", 20);
    sleep(60);
    return;

def login():
    print 'login';
    click("1574095716601.png", 20);
    sleep(30); 
    print 'login success';
    return;

def reconnect():
    print 'reconnect';
    click("1665894407351.png", 5);
    sleep(10);
    return;

def logout():
    print 'logout';
    type(Key.ESC);
    sleep(1);
    type(Key.ESC);
    sleep(1);
    type(Key.ESC);
    sleep(1);
    type(Key.ESC);
    sleep(3);
    return;

def guaji():
    print 'run';
    type(Key.SPACE);
    sleep(10);
    return;

while True:
    if exists("1574096829952.png", 5):
        guaji();
    elif exists("1574096724785.png", 5):
        gameStart();
    elif exists("1667632021664.png", 5):
        click("1667632021664.png");
        sleep(3);
    elif exists("1667929312740.png", 5):
        click("1667929312740.png",5);
        sleep(3);
    elif exists("1667632055950.png", 5):
        print 'rl';
        click("1667632055950.png");
        sleep(10);
    elif exists("1665894407351.png", 5):
        reconnect();
    elif exists("1574095716601.png", 5):
        login();
    else:
        sleep(10);