import vobject

vCard = vobject.vCard()
vCard.add('N').value = vobject.vcard.Name(family='Simpson', given='Homer')
vCard.add('FN').value = "Homer Simpson"
vCard.add('BDAY').value = '1956-05-12'

vCard.add('EMAIL')
vCard.email.value = 'chunkylover53@aol.com'
vCard.email.type_param = 'INTERNET'

vCard.add('ADR')
vCard.adr.value = vobject.vcard.Address('742 Evergreen Terrace','Springfield','OR','58008','U.S.A.')
vCard.adr.type_param = 'HOME'

vCard.add('TEL')
vCard.tel.value = '+1-939-555-0113'
vCard.tel.type_param = 'HOME'

with open('HomerSimpson.vcf', 'w') as writer:
    writer.write(vCard.serialize())
