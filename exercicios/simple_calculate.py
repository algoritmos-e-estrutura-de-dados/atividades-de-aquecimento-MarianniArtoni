cod1 = int(input())
und1 = int(input())
prec1 = round(float(input()),2)

cod2 = int(input())
und2 = int(input())
prec2 = round(float(input()),2)

print(f"Valor a pagar: R$ {round((und1*prec1)+(und2*prec2),2)}")
