def greatdivisor():
  number = int(input("Ievadiet jūsu skaitli: "))
  greatdiv = []
  for i in range(1, number + 1):
    if number % i == 0:
      greatdiv.append(i)
  print("\n")
  print("Šie ir visi jūsu skaitļa veselie dalītāji : ", greatdiv)
  print("Un šī ir jūsu veselo dalītāju summa : ", sum(greatdiv))


def alldivisor():
  skaitlis = int(input("Ievadiet jūsu 1.skaitli: "))
  skaitlis2 = int(input("Ievadiet jūsu 2.skaitli: "))
  numberr = range(skaitlis, skaitlis2 + 1)
  alldiv = []
  meow = []
  result = []
  for n in numberr:
    alldiv.append(n)
  print("\n")
  print("Šīs ir jūsu skaitļu diapazons : ", alldiv)

  for every in alldiv:
    for i in range(1, alldiv[len(alldiv) - 1] + 1):
      n = 0
      if every % i == 0:
        meow.append(i)
      result = []

  for i in meow:
    if i not in result:
      result.append(i)


  print("Šī ir jūsu skaitļu diapazona visi veselie dalītāji : ", sorted(result))



if __name__ == '__main__':



  print("\n")
  print("Sveiks, jūs sveicina -uzzini dalitaju- programma, šeit jūs varēsiet uzzināt visus noteiktā skaitļa veseļos dalītājus un tās summu.")
  print("1.funkcija - 1 skaitlis, kuram jūs uzzināsiet visus dalītājus un tos summu.")
  print("2.funkcija - logīka paliek tā paša, tikai mainās skaitļu skaits, no viena skaitļa līdz otram.")
  a = int(input("No sākuma jums vajag izvēlēties funkciju (1,2) - "))
  if a == 1:
    greatdivisor()

  elif a == 2:
    alldivisor()

  else:
    print("Nepareizi ievadīta funkcija(1,2)")
