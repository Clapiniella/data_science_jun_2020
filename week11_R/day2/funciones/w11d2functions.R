# WEEK 11 - day 2 FUNCTIONS

############
# IF/ELSE  #
############

# Cuando son caracteres ordena por orden alfabetico
"Hello" > "Goodbye"

# T es leido por R como 1 y F como 0
TRUE < FALSE

## EJEMPLO VECTORES
# Visitas a tu linkedin y a tu facebook

linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)
names(linkedin) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
names(facebook) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Dias en los que eres mas popular
linkedin[linkedin > 15]

# Dias en los que mejor no publicar que buscas trabajo
linkedin[linkedin < 5]

# ¿Cuando linkedin recibe mas visitas que facebook?
linkedin[linkedin > facebook]

## EJEMPLO MATRIZ

views <- matrix(c(linkedin, facebook), nrow = 2, byrow = TRUE)
rownames(views) <- c("linkedin", "facebook")
colnames(views) <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
views

# When does views equal 13?
views == 13

# When is views less than or equal to 14?
views <= 14

## FUNCION IFELSE

v = c(14,7,6,9,2)
ifelse(v %% 2 == 1,"odd","even")


## IF/ELSE

ifi <- 42

if (ifi < 0) {
  print("Negative number")
} else if (ifi > 0 & ifi < 50) {
  print("Mi numero")
} else
  print("Zero")


########
# FOR  #
########

# EJEMPLO BREAK

cities <- c("New York", "Paris", "London", "Tokyo", "Rio de Janeiro", "Cape Town")

for (city in cities){
  if(nchar(city)==6){
    break
  }
  print(city)
}

# EJEMPLO NEXT

for (city in cities){
  if(nchar(city)==6){
    next
  }
  print(city)
}

#The break statement abandons the active loop: 
#the remaining code in the loop is skipped and the loop is not iterated over anymore.
#The next statement skips the remainder of the code in the loop, 
#but continues the iteration.

# EJEMPLO CON RANGO

for (i in 1:length(cities)) {
  print(paste(cities[i], "is on position", i, "in the cities vector"))
}

# EJEMPLO DOBLE FOR

values <- c("O", NA, "X", NA, "O", "O", "X", NA, "X")
ttt <- matrix(values, nrow = 3, byrow = TRUE)
ttt

# define the double for loop the tic-tac-toe matrix
for (i in 1:nrow(ttt)) {
  for (j in 1:ncol(ttt)) {
    print(paste("On row", i,"and column", j, "the board contains",ttt[i,j]))
  }
}


# EJEMPLO FOR E IF/ELSE

for (li in linkedin) {
  if (li > 10) {
    print("You're popular!")
  } else {
    print("Be more visible!")
  }
  if (li > 16){
    print("This is ridiculous, I'm outta here!")
    break
  }
  if (li < 5){
    print("This is too embarrassing!")
    next
  }
  print(li)
}

# OTRO EJEMPLO FOR E IF/ELSE

rquote <- "strsplit devuelve una lista"
chars <- strsplit(rquote, split = "")[[1]]

rcount <- 0

for (char in chars) {
  if(char == "s"){
    rcount <- rcount + 1
  }
  if(char == "u"){
    break
  }
}

rcount


##########
# WHILE  #
##########

# AVISA CUANDO SEA DIVISIBLE ENTRE 8

i <- 1

while (i <= 10) {
  print(3*i)
  if (3*i %% 8 ==0) {
    print(paste(i*3, "is divisible by 8"))
    break
  }
  i <- i + 1
}

# CONTROL DE VELOCIDAD

speed <- 88

while (speed > 30) {
  print(paste("Your speed is", speed))
  
  # Break the while loop when speed exceeds 80
  if (speed > 80) {
    break
  }
  
  if (speed > 48) {
    print("Slow down big time!")
    speed <- speed - 11
  } else {
    print("Slow down!")
    speed <- speed - 6
  }
}



##############
# FUNCTIONS  #
##############

# ¿Qué cosas sabemos de las funciones?
# por favor, respuestas :) 


# una funcion que dados dos numeros, devuelva la suma

adding <- function(x, y){
  x+y 
}

# dado un vector nos devuelva los valores por encima de 10

above10 <- function(x){
  use <- x > 10
  x[use]
}

# dado un vector nos devuelva los valores mayores a un numero dado
# valor por defecto 10

above <- function(x, n = 10){
  use <- x > n
  x[use]
}

# antes de seguir
# puede sernos de gran utilidad en el ejemplo siguiente

values_w <- c(1,2,3,4,5)
values <- c(1,4,5,NA)

# calculamos su desviacion estandar

sd(values_w)
sd(values)

# elimina los nan
sd(values, na.rm=TRUE)


# coge una matriz y calcula la media de cada columna

columnmean <- function(y, removeNA = TRUE) {
  nc <- ncol(y)
  means <- numeric(nc)
  for(i in 1:nc){
    means[i] <- mean(y[,i], na.rm = removeNA)
  }
  means
}
columnmean(airquality)

# dado un numero devuelve su cuadrado

pow_two <- function(x, print_info = TRUE) {
  y <- x ^ 2
  if(print_info==TRUE){
    print(paste(x, "elevado al cuadrado igual a", y))
  }
  return(y)
}

# tira dos dados

dado <- function() {
  posibilidades <- 1:6
  dice <- sample(posibilidades, size = 1)
  dice
}


# define una funcion que dado un numero me devuelva un mensaje
interpret <- function(num_views) {
  if (num_views > 15) {
    print("You're popular!")
    return(num_views)
  } else {
    print("Try to be more visible!")
    return(0)
  }
}

# define una funcion que use interpret, donde
# views: es un vector con datos a interpretar
# return_sum: el total de visitas obtenidos en los dias mas populares
interpret_all <- function(views, return_sum=TRUE) {
  count <- 0
  
  for (v in views) {
    count = count + interpret(v)
  }
  
  if (return_sum==TRUE) {
    return(count)
    
  } else {
    return(NULL)
  }
}

# pruebo con los vectores linkedin y facebook

interpret_all(linkedin)
interpret_all(facebook)


#################
# LAPPLY/SAPPLY #
#################

pioneers <- c("GAUSS:1777", "BAYES:1702", "PASCAL:1623", "PEARSON:1857")

# separa los nombres y sus años de nacimiento
split_math <- strsplit(pioneers, split = ":")

# pasa los nombres a minuscula: split_low
split_low <- lapply(split_math, tolower)


## FUNCIONES ANÓNIMAS

# funcion normal
triple <- function(x) { 3 * x }

# funcion anonima 
function(x) { 3 * x }

# utiliza la funcion anonima con un lapply
lapply(c(1,2,3), function(x) { 3 * x })


# aplicar la funcion class a todos los elementos de una lista 

nyc <- list(pop = 8405837,
            boroughs = c("Manhattan", "Bronx", "Brooklyn",
                         "Queens", "Staten Island"),
            capital = FALSE)

class(nyc)

lapply(nyc,class)


# ¿Te has fijado que lapply siempre devuelve una lista?

# para convertir una lista a un vector
unlist(lapply(split_math, nchar))

# alternativa (vector/matriz)
sapply(split_math, nchar)


# TEMPERATURA BAJO CERO

temp <- list(c(1,4,5,6,7),c(7,2,8,4,9), c(-1,5,7,-8,4), c(7,-5,4,3,-2))

bajocero <- function(x) {
  return(x[x < 0])
}

# Con sapply(): freezing_s
freezing_s <- sapply(temp, bajocero)


# Con lapply(): freezing_l
freezing_l <- lapply(temp, bajocero)

# ¿Son iguales?
identical(freezing_l, freezing_s)


# queremos que nos avise de la temperatura media
print_info <- function(x) {
  cat("The average temperature is", mean(x), "\n")
}

# Con sapply()
sapply(temp, print_info)

# Con lapply()
lapply(temp, print_info)





