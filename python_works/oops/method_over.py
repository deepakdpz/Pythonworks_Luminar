class Calculator:

    # def add(self,n1,n2):         #
    #     return n1+n2             #
    #                              #
    # def add(self,n1,n2,n3):      #
    #     return n1+n2+n3          #=======>method overlapping
    #                              #
    # def add(self,n1,n2,n3,n4):   #
    #     return n1+n2+n3+n4       #
                                   #

      def add(self,*args):
            return sum(args)                           

obj=Calculator()

print(obj.add(100,200))