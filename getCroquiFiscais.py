# EM DESENVOLVIMENTO
import iface


# Obtem as feições selecionadas de uma camada.
selectedFeatures = iface.activeLayer().selectedFeatures()

# Obtem os valores distintos de SQ, somente do é do tipo fiscal
SQ = set()
for feature in selectedFeatures:
    if feature['qd_tipo'] == 'F':
        SQ.add(feature['qd_setor']+feature['qd_fiscal'])






# Provedores
prov_PRODAM = 'http://sf9402.app.prodam/intranet/frmConsultaCroquiPDF.aspx?pstrSetor={}&pstrQuadra={}'
prov_PUBLICO = ''

#############################################################
# Retorna um SQ dividido por ponto
for feature in selectedFeatures[:5]:
    print(feature['qd_setor']+'.'+feature['qd_fiscal'])


# Obtem os valores distintos de SETOR
SETOR = set()
for feature in selectedFeatures:
    SETOR.add(feature['qd_setor'])
    
# Obtem os valores distintos de SQ
SQ = set()
for feature in selectedFeatures:
    SQ.add(feature['qd_setor']+feature['qd_fiscal'])
