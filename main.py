import argparse
from pyad import aduser
from pyad import pyad
import win32api
import win32net
import win32security

# [START run]
def main(user, status):

    desc = win32security.GetFileSecurity(
        ".", win32security.OWNER_SECURITY_INFORMATION
    )
    sid = desc.GetSecurityDescriptorOwner()

    # https://www.programcreek.com/python/example/71691/win32security.ConvertSidToStringSid
    sidstr = win32security.ConvertSidToStringSid(sid)
    print("Sid is", sidstr)

    user_info = win32net.NetUserGetInfo(win32net.NetGetAnyDCName(), win32api.GetUserName(), 2)
    full_name = user_info["full_name"]
    #print(user_info)

    print('User Information:')
    pyad.set_defaults(ldap_server="SUSCAAPE01.TI.ads", username="juan.cruz2", password="Corona2022@")
    user = pyad.aduser.ADUser.from_cn(full_name)

    print(user.displayName)
    print(user.description)
    print(user.UserAccountControl)
    user.set_user_account_control_setting("ACCOUNTDISABLE", True)
    #attr = user.get_allowed_attributes()
    #print(attr)
    #user.update_attribute('company', 'Telus', no_flush=False)
    #user.disable()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('user', help='The user name.')
    parser.add_argument('status', help='The new status.')

    args = parser.parse_args()

    main(args.user,args.status)
# [END run]
#python main.py juan.cruz2 status
