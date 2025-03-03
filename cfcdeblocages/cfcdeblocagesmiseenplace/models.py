from django.db import models

# Events type class model
class Type_evenement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return(f"{self.libele}")

# Next events class model
class Evenement_suivant(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return(f"{self.libele}")
    
# Events class model
class Evenement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    datedebut = models.CharField(max_length=100)
    datefin = models.CharField(max_length=100)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    typeevenement = models.ForeignKey(Type_evenement, on_delete=models.CASCADE)
    evenementsuivant = models.ForeignKey(Evenement_suivant, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.libele}")

# Alerts type class model
class Type_alerte(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return(f"{self.libele}")

# Alerts class model
class Alerte(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    declencheur = models.CharField(max_length=100)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    typealerte = models.ForeignKey(Type_alerte, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.libele}")
    
# Loan type class model
class Type_de_pret(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    productcode = models.CharField(max_length=100)
    libele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return(f"{self.libele}")

# Loan file class model
class Dossier_de_pret(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unitcode = models.CharField(max_length=100)
    clientcode = models.CharField(max_length=100)
    fullname = models.CharField(max_length=255)
    reference = models.CharField(max_length=100)
    capitalnominal = models.CharField(max_length=100)
    maxterm = models.CharField(max_length=100)
    externalrib = models.CharField(max_length=100)
    externalribbankcode = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    rib = models.CharField(max_length=100)
    bankcode = models.CharField(max_length=100)
    udate = models.DateField()
    cdate = models.DateField()
    franchiseduration = models.CharField(max_length=100)
    agreementdate = models.DateField() 
    datefirstallotement = models.DateField()
    echpremi = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    statusdate = models.DateField()
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    productcode = models.ForeignKey(Type_de_pret, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.fullname}")

# Loan conditions class model
class Conditions_primo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    libele = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    productcode = models.ForeignKey(Type_de_pret, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.libele}")