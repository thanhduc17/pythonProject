from bai_tap.sv import SinhVien
import os
import pickle
def ghi_sv(tm: str, ten_tt: str, sv: SinhVien):

    try:
        f = open(os.path.join(tm, ten_tt), 'wb')
        pickle.dump(sv, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print('Xay ra loi trong qua trinh ghi file')

def doc_sv(tm: str, ten_tt: str) :
    try:
        f = open(os.path.join(tm, ten_tt), 'rb')
        content = f.readlines()
        f.close()
        print("đọc thành công")
        return content
    except Exception as e:
        print("đọc thất bại")
        return  e
