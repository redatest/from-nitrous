# Year choices
from django.utils.translation import ugettext_lazy as _

# YEARS_CHOICES = [('all', 'ALL')]
# for y in range(1970,2015):        
# 	YEARS_CHOICES.append(tuple([y, y]))        

# YEARS_CHOICES.append(('all', _('ALL')))
# YEARS_CHOICES.sort(reverse = True)
# YEARS_CHOICES.pop(0)
# YEARS_CHOICES = tuple(YEARS_CHOICES)

# price choices
SALARY_CHOICES = [
	('all', _('ALL')),
	('0', '0'),
	('1', '500'),
	('2', '1000'),
	('3', '2000'),
	('4', '3000'),
	('5', '4000'),
	('6', '5000'),
	('7', '6000'),
	('8', '7000'),
	('9', '8000'),
	('10', '9000'),
	('11', '10000'),
	('12', '15000'),
	('13', '20000'),
	('14', '25000'),
	('15', '30000'),
	('16', '35000'),
	('17', '40000'),
	('18', '45000'),
	('19', '50000'),
	('20', '55000'),
	('21', '60000'),
	('22', '65000'),
	('23', '70000'),
	('24', '75000'),
	('25', '80000'),
	('26', '85000'),
	('27', '90000'),
	('28', '95000'),
	('29', '100000'),
	('30', '125000'),
	('31', '150000'),
	('32', '175000'),
	('33', '200000'),
	('34', '250000'),
	('35', '300000'),
	('36', '350000'),
	('37', '400000'),
	('38', '450000'),
	('39', '500000'),
	('40', '750000'),
	('41', '1000000')
]

OFFER_CHOICES = [
	('all', _('ALL')),
	('1', _('Freelane')),
	('2', _('CDD')),
	('3', _('CDI')),
	('4', _('Stage'))
]

CATEGORY_CHOICES = [('all', _('ALL')), 
	('1', _('Finance')),
	('2', _('Marketing')),
	('3', _('Batiments')),
	('4', _('Immobilier')),
	('5', _('Engineering')),
	('6', _('Informatique'))
]

REGION_CHOICES = [ 
	('all', _('ALL')),
	('1', _('Ile de france')), 
	('2', _('Aube')), 
	('3', _('Auvergne')), 
	('4', _('PACA')), 
	('5', _('Picardie')), 
	('6', _('Bretagne'))
]


YESNO = [
    ('Used', _('Yes')),
    ('New',  _('No'))
]
