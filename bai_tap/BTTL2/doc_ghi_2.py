
from bai_tap.sv import SinhVien
import os
import pickle

def ghi_sv(tm: str, ten_tt: str, nsv: list[SinhVien]):
    try:
        f=open(os.path.join(tm, ten_tt), 'wb')
        pickle.dump(nsv, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print(e)
        print('Xay ra loi trong qua trinh ghi file')

def doc_sv(thumuc: str, ten_taptin: str) -> list[SinhVien]:
    try:
        f = open(os.path.join(thumuc, ten_taptin), 'rb')
        sv = pickle.load(f)
        return sv
    except Exception as e:
        print(e)


def in_ra_cac_sv(sv: list[SinhVien]):
    for i in sv:
        print(i)



