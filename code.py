import tkinter
import time
import random
import numpy as np
from numba import jit


class App():
    def __init__(self, root):
        self.root = root
        self.font_la = "Serif 14"
        self.font_me = "Serif 13"
        self.font_sm = "Serif 12"
        self.root.title("Ομάδα 06")
        self.widgets()

    def widgets(self):

                #######Δημιουργία των παραθύρων#######

        wid1 = tkinter.Frame(self.root)
        
        wid1.pack(fill='both', expand=1)
        
        
        self.entryText = tkinter.StringVar()

        self._box = tkinter.Text(wid1,
                                width=15,
                                height=1,font=self.font_sm,
                                bg='#DEFDFB')
                                      
        self._box.place(x=0,
        y=445)

        

                #######Δημιουργία των Labels####### 


        label1=tkinter.Label(wid1, text="Πολλαπλασιασμός Πινάκων:",
                            font=self.font_me)

        label1.place(x=0,
        y=0)

        
        label2=tkinter.Label(wid1, text="Αναστροφη πίνακα:",
                            font=self.font_me)

        label2.place(x=0,
        y=60)

        label3=tkinter.Label(wid1, text="Εύρεση Πολλαπλασίων Στον Πίνακα Αθροίσματος:",
                            font=self.font_me)

        label3.place(x=0,
        y=120)

        
        label4=tkinter.Label(wid1, text="Εύρεση ορίζουσας:",
        font=self.font_me)

        label4.place(x=0,
        y=180)

        
        label5=tkinter.Label(wid1, text="Εύρεση LU:",
                            font=self.font_me)

        label5.place(x=0,
        y=240)

        label6=tkinter.Label(wid1, text="Πρόσθεση Πινάκων:",
                            font=self.font_me)

        label6.place(x=0,
        y=300)
        

        label7=tkinter.Label(wid1, text="Χρόνος που χρειάστηκε για την εκτέλεση της πράξης:",
                            font=self.font_me)

        label7.place(x=0,
        y=420)


            #######Δημιουργία των Buttons


        button_matrixmult = tkinter.Button(wid1, text="με Python",
                                    font=self.font_me,
                                    bg='#DBFDF7',
                                    command=self.matrixmult)
                                         
        button_matrixmult.place(x=0,
                              y=25)

        button_matrixmult2 = tkinter.Button(wid1, text="με Numpy, Numba:",
                                    font=self.font_me,
                                    bg='#DBFDF7',
                                    command=self.matrixmult2)

        button_matrixmult2.place(x=90,
                              y=25)


        button_anastrofos = tkinter.Button(wid1, text="με Python",
                                         font=self.font_me,
                                        bg='#DBFDF7',
                                         command=self.anastrofos)
        
        button_anastrofos.place(x=0,
                                y=85)
        

        button_anastrofos2 = tkinter.Button(wid1, text="με Numpy, Numba",
                                        font=self.font_me,
                                        bg='#DBFDF7',
                                        command=self.anastrofos2)
        

        button_anastrofos2.place(x=90,
                                y=85)




        button_pollaplasia = tkinter.Button(wid1, text="με Python",
                                           font=self.font_me,
                                        bg='#DBFDF7',
                                           command=self.pollaplasia)
                                                    
        button_pollaplasia.place(x=0,
                                y=145)

        button_pollaplasia2 = tkinter.Button(wid1, text="με Numpy, Numba",
                                            font=self.font_me,
                                            bg='#DBFDF7',
                                            command=self.pollaplasia2)
                                                    
        button_pollaplasia2.place(x=90,
                                y=145)

       


        button_orizousa = tkinter.Button(wid1, text="με Python",
                                        font=self.font_me,
                                        bg='#DBFDF7',
                                        command=self.orizousa)
        button_orizousa.place(x=0,
                             y=205)

        button_orizousa2 = tkinter.Button(wid1, text="με Numpy, Numba",
                                        font=self.font_me,
                                        bg='#DBFDF7',
                                        command=self.orizousa2)
        button_orizousa2.place(x=90,
                             y=205)


        button_lu = tkinter.Button(wid1, text="με Python",
                                        font=self.font_me,
                                        bg='#DBFDF7',
                                        command=self.lu)
        

        button_lu.place(x=0,
                        y=265)


        button_lu2 = tkinter.Button(wid1, text="με Numpy, Numba",
                                        font=self.font_me,
                                        bg='#DBFDF7',
                                        command=self.lu2)
        

        button_lu2.place(x=90,
                        y=265)


        button_prosthesi = tkinter.Button(wid1, text="με Python",
                                        font=self.font_me,
                                        bg='#DBFDF7',
                                        command=self.prosthesi)
        

        button_prosthesi.place(x=0,
                        y=325)


        button_prosthesi2 = tkinter.Button(wid1, text="με Numpy, Numba",
                                        font=self.font_me,
                                        bg='#DBFDF7',
                                        command=self.prosthesi2)
        

        button_prosthesi2.place(x=90,
                                y=325)



                                               ######Πράξεις#######



    def matrixmult(self): #κώδικας υπολογισμού γινομένου δύο τυχαίων πινάκων 500*500  με σκέτη Python
        def random_matrix(rows, columns, low = 0, high = 100): #δημιουργία τυχαίου πίνακα
            matrix = [[random.randint(low, high) for c in range(columns)] for r in range(rows)] #επιστρέφει έναν rows x columns πίνακα με τυχαίους ακέραιους αριθμούς(από το 0 μέχρι το 100)
            return matrix
            pass

        start = time.time()
        def mult_matrix(A,L,r1,c1,r2,c2): #γινόμενο πινάκων: r1=γραμμή 1ου πίνακα  , r2=γραμμή 2ου πίνακα , c1=στήλη 1ου πίνακα  , c2=στήλη 2ου πίνακα 
            B=[]
            for i in range(c2):
                B.append([])
            for i in range(c2):
                for j in range(r2):
                    B[i].append(L[j][i])
            V=[]
            for i in range(r1):
                V.append([])
            for k in range(r1):
                for i in range(c2):
                    s=0
                    for j in range(c1):
                        s += A[k][j]*B[i][j]
                    V[k].append(s)
            return V
            pass
                
        rows1 = 500
        columns1 = 500
        rows2 = 500
        columns2 = 500

        X = random_matrix(rows1,columns1) #τυχαίος 1ος πίνακας 500*500
        Y = random_matrix(rows2,columns2) #τυχαίος 2ος πίνακας 500*500
        Z = mult_matrix(X,Y,rows1,columns1,rows2,columns2) #πολλαπλασιασμός των 2 τυχαίων πινάκων

        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))


    def matrixmult2(self):  #κώδικας υπολογισμού γινομένου δύο τυχαίων πινάκων 500*500 με Numba, Numpy
        a = np.array([[random.randint(0,100) for i in range(1,501)] for j in range(1,501)])
        b = np.array([[random.randint(0,100) for i in range(1,501)] for j in range(1,501)])


        start = time.time()
        z=np.dot(a,b)
        end = time.time()

        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end - start)*1000)))






    def pollaplasia(self): #κώδικας εύρεσης κοινών πολλαπλασίων σε πίνακα 500*500 με σκέτη Python
        start = time.time()

        L = []
        M = []

        for i in range(500):
            L.append([])
            M.append([])
            for j in range(500):
                L[i].append(j + 1)
                M[i].append(j + 1)

        N = []

        for i in range(500):
            N.append([])
            for j in range(500):
                N[i].append(L[i][j] + M[i][j])

        for i in range(500):
            for j in range(500):
                N[i][j]
                # print(N[i][j], end=' ')
            #print('\n')


        L3 = []  #δημιουργούμε μία κενή λίστα L3=[]
        k = 1

        for j in N:#για κάθε ακέραιο αριθμό k από το ένα μέχρι και το δέκα (for k in range(1,11)) 
                     # εξετάζουμε για κάθε στοιχείο ανά σειρά στον πίνακα του αθροίσματος που είχε προκύψει από την πρόσθεση των πινάκων
            for num in j:
                if num % k == 0:
                    L3.append(num)
                    pass
                    #print('{} is multiple of {}'.format(num, k))
            k += 1
            if k == 11: break

        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))



    def pollaplasia2(self):  #κώδικας εύρεσης κοινών πολλαπλασίων σε τυχαίο πίνακα 500*500 με Numpy, Numba
        def numpy_sum():
            a = np.zeros([500, 500])
            for i in range(len(a)):
                a[i] = np.arange(1, 501)

            b = np.copy(a)

            c = a + b
            return c


        c = numpy_sum()
        
        
        @jit(nopython=True)#για την επιτάχυνση του παρακάτω προγράμματος που ακολουθεί
        def multiples(c):
            for k in range(1, 11): #για κάθε ακέραιο αριθμό k από το 1 μέχρι και το 10
                for num in np.nditer(c):#για να περάσουμε και να εξετάσουμε αν διαιρούνται ακριβώς οι αριθμοί ανά σειρά του πίνακά μας
                    if num % k == 0:
                        pass
                k += 1
                if k == 11: break

        start = time.time()
        m = multiples(c)
        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))





    def anastrofos(self): #κώδικας εύρεσης του ανάστροφου ενός τυχαίου πίνακα 500*500 με σκέτη Python
        x = np.array([[random.randint(0,100) for i in range(1,501)] for j in range(1,501)])
        y=np.ones( (500,500), dtype=np.int16 )


        def transpoze(x,y):  #συνάρτηση που κάνει αναστροφή του πίνακα
            for i in range(len(x)): #ελέγχει εάν όλες οι σειρές του πίνακα έχουν το ίδιο μήκος
                if len(x[i])!=len(x[0]): return 'error'
            for i in range(len(x[0])):
                for j in range(len(x)):
                    y[i][j]=x[j][i] # παίρνει τα στοιχεία του πίνακα x και τα εισάγει στον y με τέτοιο τρόπο ώστε ο y να είναι ανάστροφος του x.

        start=time.time()
        transpoze(x,y)
        end=time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))



    def anastrofos2(self): #κώδικας εύρεσης του ανάστροφου ενός τυχαίου πίνακα 500*500 με Numpy, Numba
        x = np.array([[random.randint(0,100) for i in range(1,501)] for j in range(1,501)])
        y=np.ones( (500,500), dtype=np.int16 )

        @jit
        def transpoze(x,y):  #συνάρτηση που κάνει αναστροφή του πίνακα
            for i in range(len(x)):#ελέγχει εάν όλες οι σειρές του πίνακα έχουν το ίδιο μήκος
                if len(x[i])!=len(x[0]): return 'error'
            for i in range(len(x[0])):
                for j in range(len(x)):
                    y[i][j]=x[j][i]# παίρνει τα στοιχεία του πίνακα x και τα εισάγει στον y με τέτοιο τρόπο ώστε ο y να είναι ανάστροφος του x.

        start=time.time()
        transpoze(x,y)
        end=time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))





    def lu(self): #υπολογογισμός lu ενός τυχαίου πίνακα 500*500 με σκέτη Python
        A = np.round(np.random.rand(1000, 1000)*10) #δημιουργία δύο πινάκων 1000*1000
        B = np.round(np.random.rand(1000)*10)

        def LUdecomp(x): #συνάρτηση που αναλύει τον πίνακα Α σε πίνακες L/U
            n = len(x)
            for k in range(0,n-1):
                for i in range(k+1,n):
                    if x[i,k] != 0.0:
                        lam = x [i,k]/x[k,k]
                        x[i,k+1:n] = x[i,k+1:n] - lam*x[k,k+1:n]
                        x[i,k] = lam
            return x

        def LUsolve(x,y): #επίλυση του συστήματος
            n = len(x)
            for i in range(1,n):
                y[i] =y[i]-np.dot(x[i,0:i],y[0:i])
            y[n-1] = y[n-1]/x[n-1,n-1]
            for i in range(n-2,-1,-1):
                y[i] = (y[i] - np.dot(x[i,i+1:n],y[i+1:n]))/x[i,i]
            return y

        start=time.time()
        LU = LUdecomp(A)
        LUsolve(LU,B)
        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))



    def lu2(self): #υπολογογισμός lu ενός τυχαίου πίνακα 500*500 με Numpy, Numba
        A = np.round(np.random.rand(1000, 1000)*10) #δημιουργία δύο πινάκων 1000*1000
        B = np.round(np.random.rand(1000)*10)

        @jit
        def LUdecomp(x):#συνάρτηση που αναλύει τον πίνακα Α σε πίνακες L/U
            n = len(x)
            for k in range(0,n-1):
                for i in range(k+1,n):
                    if x[i,k] != 0.0:
                        lam = x [i,k]/x[k,k]
                        x[i,k+1:n] = x[i,k+1:n] - lam*x[k,k+1:n]
                        x[i,k] = lam
            return x
        
        def LUsolve(x,y): #επίλυση του συστήματος
            n = len(x)
            for i in range(1,n):
                y[i] =y[i]-np.dot(x[i,0:i],y[0:i])
            y[n-1] = y[n-1]/x[n-1,n-1]
            for i in range(n-2,-1,-1):
                y[i] = (y[i] - np.dot(x[i,i+1:n],y[i+1:n]))/x[i,i]
            return y

        start=time.time()
        LU = LUdecomp(A)
        LUsolve(LU,B)

        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))





    def orizousa(self): #υπολογογισμός ορίζουσας ενός τυχαίου πίνακα 500*500 με σκέτη Python
        start=time.time()
        def triangle(L): #για τις πράξεις-την απαλοιφή Gauss
	        for i in range(len(L) - 1): #περνάμε από την πρώτη μέχρι και την προτελευταία γραμμή του πίνακα
		        for k in range(i + 1, len(L)): #πηγαίνουμε στην αμέσως επόμενη γραμμή από αυτή που αρχικά είχαμε επιλέξει, μέχρι και την τελευταία γραμμή του πίνακα L
			        coeficient=(-L[k][i]/L[i][i]) #ορίζουμε τον παράγοντα ορίζουμε το coeficient,με τον οποίο θα πολλαπλασιάζουμε την κάθε γραμμή  i κάθε φορά, για να προκύψει σταδιακά o τριγωνικός πίνακας
			        for j in range(i, len(L[i])): #γίνεται για κάθε στοιχείο στην γραμμή k η γραμμοπράξη
				        product = L[i][j] * coeficient
				        L[k][j] += product
				        if L[i][i] == 0: #παρακάμπτουμε τις μηδενικές στήλες και μεταβαίνουμε απευθείας στο εκάστοτε στοιχείο της κύριας διαγωνίου
					        return 0
	        return L

        def create_matrix(): #για τη δημιουργία του πίνακα μας L, του οποίου και θα υπολογίσουμε την ορίζουσα
            L = []  #δημιουργία κενής λίστας L
            for i in range(500):  #για κάθε σειιρά i,από την πρώτη μέχρι και την πεντακοσιοστή ( for I in range(500)) προσθέτουμε αριθμούς από το 0 μέχρι και το 100
                L.append([])
                for j in range(500):
                    L[i].append(random.randint(0, 100))
            return L
        L=create_matrix()

        def determinant(L):
            det = 1
            
            L = triangle(L)
            if L == 0: #αν υπάρχει μηδενικό στοιχείο πάνω στην κύρια διαγώνιο, η ορίζουσα να υπολογιστεί απευθείας ίση με 0
                 det = 0
            else: #αλλιώς, πολλαπλασιάζουμε τα στοιχεία της κύριας διαγωνίου του τριγωνικού μας πίνακα, οπως αυτός προέκυψε, και έτσι υπολογίζουμε την ορίζουσά του
                for i in range(len(L)):
                    det *= L[i][i]
            return det
            #print(determinant(L))
        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))
    



    def orizousa2(self): #υπολογισμός ορίζουσας ενός τυχαίου πίνακα 500*500 με Numpy, Numba
        A= np.array([[random.randint(0,100) for i in range(1,501)] for j in range(1,501)])  #δημιουργία πίνακα 500*500 με τυχαία στοιχεία από το 0 μέχρι και το 100
        start=time.time()
        (sign, logdet) = np.linalg.slogdet(A) #υπολογισμός ορίζουσας
        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))





    def prosthesi(self): #άθροιση δύο τυχαίων πινάκων 500*500 με σκέτη Python
        L = [] #δημιουργία δύο κενών λιστών της L και της Μ
        M = []

        start=time.time()
        for i in range(500):  #ανα σειρά,για 500 επαναναλήψεις-σειρές , ομοίως και στους δύο πίνακες, προσθτίθενται διαδοχικά όλοι οι ακέαραιοι αριθμοί από τ0 1 μεχρι και το 500
            L.append([])
            M.append([])
            for j in range(500):
                L[i].append(j + 1)
                M[i].append(j + 1)

        N = [] #δημιουργία νέας κενής λίστας

        for i in range(500): #κάθε σειρά, και για τις 500 της νέας λίστας-πίνακα N
            N.append([])
            for j in range(500):
                N[i].append(L[i][j] + M[i][j]) #προστίθενται τα αντίσοιχα στοιχεία από τους παναράνω πίνακες-λίστες L και M

        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end-start)*1000)))



    def prosthesi2(self):  # άθροιση δύο τυχαίων πινάκων 500*500 με Numpy, Numba
        a = np.array([[random.randint(0,100) for i in range(1,501)] for j in range(1,501)])
        b = np.array([[random.randint(0,100) for i in range(1,501)] for j in range(1,501)])
        
        @jit
        def sum(a,b):
            c = a + b
            return c

        start=time.time()
        sum(a,b)
        end = time.time()
        self.entryText.set(time)
        self._box.delete('1.0', 'end')
        self._box.insert('end', '{} ms'.format(round((end - start) * 1000)))




def main():
    root = tkinter.Tk()
    root.wm_geometry("450x472")
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()

