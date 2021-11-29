
class Orang(object):

    def _init_(self):
        pass

class Anak:

    def _init_(self):
        pass


#class
class Mahasiswa(Orang, Anak):

    #self -> method ini adalah member dari sebuah class
    def _init_(self):
        self.nama = ''
        self.kelas = ''

    def mengerjakan_tugas(self):
        print('kerjakan tugas')


nama = 'reza'
#object
mhs = Mahasiswa()

mhs.nama = 'reza'
mhs.kelas = '4C'