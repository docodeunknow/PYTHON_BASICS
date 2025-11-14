# HYBRID INHERINTANCE

try:
    # Base class
    class A:
        def featureA(self):
            print("Feature A")

    # Class B inherits from A   (Multilevel)
    class B(A):
        def featureB(self):
            print("Feature B")

    # Another base class
    class C:
        def featureC(self):
            print("Feature C")

    # Class D inherits from B and C   (Multiple)
    class D(B, C):
        def featureD(self):
            print("Feature D")

except Exception as e:
    print(e)

else:
    d = D()

    d.featureA()  
    d.featureB()  
    d.featureC()  
    d.featureD()  

finally:
    print("HYBRID INHERINTANCE DONE !!")