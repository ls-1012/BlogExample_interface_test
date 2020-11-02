import traceback
import hashlib

def generate_username(file):
    print(file)
    try:
        with open(file,"r+")as f:

            data=int(f.read())
            f.seek(0, 0)
            f.write(str(data + 1))

        return str(data+1)
    except:
        traceback.print_exc()
        return

def get_username(file):
    with open(file)as f:
        data=f.read()

    return str(data)

def get_pwd(user):
    m5 = hashlib.md5()
    m5.update(user.encode("utf-8"))
    pwd = m5.hexdigest()
    return pwd

if __name__=='__main__':
    print(generate_username("username.txt"))