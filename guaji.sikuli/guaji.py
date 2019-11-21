def login():
    print 'login';
    if not exists("1574095716601.png"):
        print 'no login icon';
        openApp('D:\Battle.net\Battle.net.exe');
    print 'login icon';
    wait("1574095716601.png", 60);
    click("1574095716601.png",20);
    wait("1574096724785.png", 60);
    click("1574096724785.png",20);
    wait("1574096829952.png",60);
    print 'login success';
    return;

def logout():
    print 'logout';
    clcik(Pattern("1574095824831.png").targetOffset(2,37),3);
    type(Key.ESC);
    sleep(1);
    type(Key.ESC);
    sleep(3);
    return;

def guaji():
    print 'run';
    type(Key.SPACE);
    sleep(3);
    return;
    
while True:
    if exists("1574096829952.png",3):
        guaji();
    elif exists("1574095824831.png",3):
        logout();
    else:
        login();