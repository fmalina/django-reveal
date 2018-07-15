from django.shortcuts import render
from django.contrib.auth import authenticate, login
from reveal.tests.test_models import create_user

TEXT = """
Ac primo quidem loco bonum sola honestate contineri,
deinde secundo tamquam consectario ostendit honestissimum
quemque@in.se uno habere omnia bene beateque vivendi praesidia.
Ex his autem locis cetera, quae deinceps persequitur,
apta sunt et suspensa. Itaque tertius locus est de peccatorum
aequalitate omnium@Quarti.de stultorum insania loci pauca
tantum verba supersunt; cetera@exciderunt.com
titulo et initio alius paradoxi
"""


def index(request):
    """Create dummy account and login the current user
    """
    u = create_user()
    u = authenticate(username=u.username,
                     password='test*pw',
                     email='francis@vizualbod.com')
    login(request, u)

    return render(request, 'index.html', {'user': u,
                                          'text': TEXT})
