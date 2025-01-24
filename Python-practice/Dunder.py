class student:
    def __init__(self,name):
        self.name = name
    def __len__(self):
        i =0;
        for c in self.name:
            i +=1;
        return i
    def __str__(self):
        return (f"The  Name Is THe Owner is {self.name} str")
    def __repr__(self):
        return (f"The  Name Is THe Owner is {self.name} repr")
    def __call__(self, *args, **kwds):
       if args: 
            print(f"Your Input is List  : {args}")
       else:
            print(f"Your Input is Dictory  : {kwds}")
        