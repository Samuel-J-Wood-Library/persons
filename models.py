from django.db import models

class Organization(models.Model):
    # date the record was created
    record_creation = models.DateField(auto_now_add=True)

    # date the record was most recently modified
    record_update = models.DateField(auto_now=True)
    
    # formal identification/name of the organization/institution
    name = models.CharField(max_length=128, unique=True)
    
    # short name for display purposes
    short_name = models.CharField(max_length=16)
    
    # The organization's primary classification according to NAICS
    # definitions available at https://en.wikipedia.org/wiki/North_American_Industry_Classification_System 
    AGRICULTURE = "AG"
    MINING = "MI"
    UTILITIES = "UT"
    CONSTRUCTION = "CO"
    MANUFACTURING = "MF"
    WHOLESALE = "WS"
    RETAIL = "RT"
    TRANSPORT = "TR"
    INFORMATION = "IN"
    FINANCE = "FI"
    REALESTATE = "RE"
    SCIENTIFIC = "SC"
    MANAGEMENT = "MG"
    ADMIN = "AD"
    EDUCATIONAL = "ED"
    HEALTHCARE = "HC"
    ARTS = "AR"
    HOSPITALITY = "HS"
    GOVERNMENT = "GV"
    OTHER = "OT"

    NAICS_CHOICES = (
            (AGRICULTURE, "Agriculture, Forestry, Fishing and Hunting"),
            (MINING, "Mining, Quarrying, and Oil and Gas Extraction"),
            (UTILITIES, "Utilities"),
            (CONSTRUCTION, "Construction"),
            (MANUFACTURING, "Manufacturing"),
            (WHOLESALE, "Wholesale Trade"),
            (RETAIL, "Retail Trade"),
            (TRANSPORT, "Transportation and Warehousing"),
            (INFORMATION, "Information"),
            (FINANCE, "Finance and Insurance"),
            (REALESTATE, "Real Estate and Rental and Leasing"),
            (SCIENTIFIC, "Professional, Scientific, and Technical Services"),
            (MANAGEMENT, "Management of Companies and Enterprises"),
            (ADMIN, 
            "Administrative and Support and Waste Management and Remediation Services"),
            (EDUCATIONAL, "Educational Services"),
            (HEALTHCARE, "Health Care and Social Assistance"),
            (ARTS, "Arts, Entertainment, and Recreation"),
            (HOSPITALITY, "Accommodation and Food Services"),
            (GOVERNMENT, "Public Administration"),
            (OTHER, "Other Services"),
    )

    classification = models.CharField(
                            max_length=2,
                            choices = NAICS_CHOICES,
                            null=True,
                            blank=True,
    )
        
    def __str__(self):
        return "{}".format(self.name)


class Department(models.Model):
    # date the record was created
    record_creation = models.DateField(auto_now_add=True)

    # date the record was most recently modified
    record_update = models.DateField(auto_now=True)
    
    # formal identification/name of the department
    name = models.CharField(max_length=128, unique=True)
    
    # classify the department's primary role within the institution according to NACUBO
    # definitions available at http://www.buffalo.edu/administrative-services/managing-money/state-funds/create-maintain-accts/nacubo-codes.html 
    INSTRUCTION = "ID"
    ACTIVITIES = "OA"
    RESEARCH = "OR"
    SERVICE = "PS"
    LIBRARY = "LI"
    STUDENT = "SS"
    MAINTENANCE = "MP"
    GENADMIN = "GA"
    GENINST = "GI"
    AUXILARY = "AE"
    CLINICS = "HC"
    FELLOWSHIPS = "SF"
    ADDITIONAL = "AC"
    NACUBO_CHOICES = (
                (INSTRUCTION, "Instruction and Department Research",),
                (ACTIVITIES, "Organized Activities",),
                (RESEARCH, "Organized Research",),
                (SERVICE, "Public Service",),
                (LIBRARY, "Libraries",),
                (STUDENT, "Student Services",),
                (MAINTENANCE, "Maintenance and Operation of Physical Plant",),
                (GENADMIN, "General Administration",),
                (GENINST, "General Institutional Services",),
                (AUXILARY, "Auxilary Enterprises",),
                (CLINICS, "Hospitals and Clinics",),
                (FELLOWSHIPS, "Scholarships and Fellowships",),
                (ADDITIONAL, "Additional Classifications",),
    )
    classification = models.CharField(
                            max_length=2,
                            choices = NACUBO_CHOICES,
                            null=True,
                            blank=True,
    )
        
    def __str__(self):
        return "{}".format(self.name)

class Role(models.Model):
    # unique name identifying the role
    name = models.CharField(max_length=128, unique=True)
    
    def __str__(self):
        return "{}".format(self.name)

   
class Person(models.Model):
    # date the record was created
    record_creation = models.DateField(auto_now_add=True)
    # date the record was most recently modified
    record_update = models.DateField(auto_now=True)
    
    # a unique institutional identifier for the individual
    cwid = models.CharField(max_length=16, unique=True, null=True, blank=True)
    
    # individual's preferred name, (includes first and last)
    preferred_name = models.CharField(  max_length=128,
                                        null=True,
                                        blank=True,
    )
    
    # individual's first name
    first_name = models.CharField(max_length=32)
    
    # individual's last name
    last_name = models.CharField(max_length=32)
    
    # individual's preferred pronoun
    HEHIM = "HH"
    SHEHER = "SH"
    THEYTHEM = "TT"
    ZIEZIM = "ZZ"
    OTHER = "OT"
    PRONOUN_CHOICES = (
                        (HEHIM, "He/Him/His"),
                        (SHEHER, "She/Her/Hers"),
                        (THEYTHEM, "They/Them/Theirs"),
                        (ZIEZIM, "Zie/Zim/Zir"),
                        (OTHER, "Other identification"),
    )
    pronoun = models.CharField(
                            max_length=2,
                            choices = PRONOUN_CHOICES,
                            null=True,
                            blank=True,
    )
    
    # individual's title of reference
    MR = "MR"
    MRS = "MS"
    MISS = "MI"
    MS = "MZ"
    DR = "DR"
    REV = "RV"
    SIR = "SR"
    TITLE_CHOICES = (
                (DR, "Dr")
                (MR, "Mr"),
                (MRS, "Mrs"),
                (MISS, "Miss"),
                (MS, "Ms"),
                (REV, "Rev"),
                (SIR, "Sir") 
                
    )
    title = models.CharField(
                            max_length=2,
                            choices=TITLE_CHOICES,
                            null=True,
                            blank=True,
    )
    
    # primary contact email
    email_primary = models.EmailField("Primary email address", 
                                        null=True, 
                                        blank=True
    )
    
    # secondary contact email
    email_secondary = models.EmailField("Secondary email address", 
                                        null=True, 
                                        blank=True
    )
    
    # phone number
    phone = models.CharField(
                            max_length=32,
                            null = True,
                            blank=True,
    )
    
    

    # organization the individual is affiliated with / employed by
    organization = models.ForeignKey(Organization, 
                                    null=True, 
                                    blank=True, 
                                    on_delete=models.CASCADE,)

    # department the individual is affiliated with / employed by
    department = models.ForeignKey(Department, 
                                    null=True, 
                                    blank=True, 
                                    on_delete=models.CASCADE,)
    
    # role the individual plays within the department / project / organization
    role = models.ForeignKey(Role, 
                             null=True, 
                             blank=True, 
                             on_delete=models.CASCADE,)
    
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.preferred_name:
            name = self.preferred_name
        else:
            name = "{} {}".format(self.first_name, self.last_name)
        if self.cwid:
            id = self.cwid
        else:
            id = "---"
        
        return "{} ({})".format(name, id)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def get_absolute_url(self):
        return reverse('persons:person-details', kwargs={'pk': self.pk})