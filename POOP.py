
coche_alejandro = {"marca": "Lamborghini", "ruedas": 4, "Motor": "16c", "Color": "Rojo", "tipo":"coche"}
coche_irene = {"marca": "Ford Fiesta", "ruedas": 4, "Motor": "Normalito", "Color": "Blanco", "tipo":"coche"}
coche_marco = {"marca": "McLaren", "ruedas": 4, "Motor": "Eléctrico", "Color": "Azul", "tipo":"coche"}
coche_hugo = {"marca": "Toyota", "ruedas": 4, "Motor": "16c", "Color": "Blanco", "tipo":"coche"}

coches = [coche_alejandro, coche_irene, coche_marco, coche_hugo]

print("objetos creados sin el constructor\n")
for coche in coches:
    print(coche)


def constructorCoches(marca, motor, color):

    objeto = {  "marca": marca,
                "ruedas": 4,
                "motor": motor,
                "color": color,
                "velocidad": 0,
                "tipo": "coche"
            }

    return objeto

def getMarca(coche):
    return coche["marca"]

def setMarca(coche, nueva_marca):
    coche["marca"] = nueva_marca
    return coche

def getMotor(coche):
    return coche["motor"]

def setMotor(coche, nuevo_motor):
    coche["motor"] = nuevo_motor
    return coche


coche_alejandro1 = constructorCoches(marca = "Lamborghini", motor="16c", color="Rojo")

print("Coche Alejandro:", coche_alejandro1)

marca_alejandro = getMarca(coche_alejandro1)
print("Marca del Coche de Alejandro:", marca_alejandro)

coche_alejandro1 = setMarca(coche_alejandro1, "Wolkswagen")
print("Nueva marca del coche de Alejandro:",getMarca(coche_alejandro1))
print(coche_alejandro1)

bici = {"ruedas": 2, "color": "rojo", "velocidad": 0, "marca": "BMX", "tipo":"bicicleta"}

motor = getMotor(bici)
print(motor)




















