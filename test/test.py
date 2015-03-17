#!/usr/bin/python

# TEST SENDING COMMANDS TO SERVER:
import dbus, time, os, sys
import random

ICON = dbus.Struct((16, 16, 16*4, True, 8, 4,
                    dbus.Array((255,0,0,255) * 16 * 8 + (0,255,0,50) * 16 * 8,
                               signature="y")),
                   signature="iiibiiay")
MILLIS_SINCE_EPOCH = int(time.time() * 1000) 

def dbus_notify(nid, title, desc, hints, icon = ""):
    nid = dbus.Bus().call_blocking("org.freedesktop.Notifications",
        "/org/freedesktop/Notifications",
        "org.freedesktop.Notifications",
        "Notify",
        "susssasa{sv}i",
        ("some.app.package.name", nid, icon,
         title, desc, (), hints, 0))
    # print "notify id", nid
    return nid

def dbus_close(nid):
    dbus.Bus().call_blocking("org.freedesktop.Notifications",
                             "/org/freedesktop/Notifications",
                             "org.freedesktop.Notifications",
                             "CloseNotification",
                             "u",
                             (nid,))
               
def test_upd():
    nid = 0
    nid = dbus_notify(nid, "My title", "", {})
    time.sleep(2)
    nid = dbus_notify(nid, "My new title", "", {})
    time.sleep(2)
    nid = dbus_notify(nid, "My <u>newer</u> title", "BodyLine1\nBodyLine2",
                      {"urgency": dbus.Byte(4),
                       "when": dbus.Int64(MILLIS_SINCE_EPOCH),
                       "image-data": ICON,
                       "action_title1": "Action1",
                       "action_cmd1": "xmessage \"Msg1 Param1 Param2\"",
                       "action_title2": "Action2",
                       "action_cmd2": "xmessage \"Msg2 Param1 Param2\""})
    time.sleep(2)
    dbus_close(nid)


titles = [
    'Chuck Norris',
    'Monty Python',
    'Mickey Mouse',
    'Norah Jones'
]

descs = [
    'where is everybody?',
    'quite long msg, quite long msg, quite long msg, quite long msg, quite long msg',
    'body <b>1st</b> line\nbody 2nd line\nbody 3rd line',
    "let's party... pool party"
]

senders = [
    ('calender.png', 'Remind'),
    ('facebook.png', 'View'),
    ('telephone.png', 'Call Back'),
    ('messages.png', 'Reply')
]

def test_random(i=0):
    s = random.choice(senders)
    dbus_notify(0,
                ('%d: ') % i + random.choice(titles),
                random.choice(descs),
                { "action_title1": s[1] },
                os.getcwd() + "/images/" + s[0])
                
def test_stress(no, tout):
    for i in range(no):
        test_random(i)
        time.sleep(tout)


def test_menu():
    dbus_notify(0, "Test of action menu", "Has button, arrow and menu",
                {"urgency": dbus.Byte(4),
                 "when": dbus.Int64(MILLIS_SINCE_EPOCH),
                 "image-data": ICON,
                 "action_title" : "Reminder",
                 "action_title1": "5 min",
                 "action_cmd1": "xmessage \"5 min reminder\"",
                 "action_title2": "10 min",
                 "action_cmd2": "xmessage \"10 min reminder\""})


for arg in sys.argv[1:]:
    print arg

#test_stress()
# test_upd()
#test_menu()
# test_stress(40, 0.2)
test_stress(2, 1.2)
