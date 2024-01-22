# Math operations in Python

n1 = 5; n2 = 2;

sum = n1 + n2;
sub = n1 - n2;
mult = n1 * n2;
div = n1 / n2;
divInt = n1 // n2;
rest = n1 % n2;
exp = n1 ** n2;

print(f"The sum is: {sum}");
print(f"The sub is: {sub}");
print(f"The mult is: {mult}");
print(f"The div is: {div}");
print(f"The divInt is: {divInt}");
print(f"The rest is: {rest}");
print(f"The exp is: {exp}");

print("\n")
print("="*20)
nome = str(input("Qual eh o seu nome? "))
print(f"Prazer em te conhecer {nome:^20}!");
print(f"Prazer em te conhecer {nome:>20}!");
print(f"Prazer em te conhecer {nome:<20}!");
print(f"Prazer em te conhecer {nome:=^20}!");
