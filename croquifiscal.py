import urllib

# Definição do SQ
setor = 229
quadra = 2

# Requerimento ao endereço da prodam
url = 'http://sf9402.app.prodam/intranet/frmConsultaCroquiPDF.aspx?pstrSetor={0:0>3}&pstrQuadra={1:0>3}'.format(setor, quadra)
fileobj = urllib.request.urlopen (url)

# Cria um novo arquivo e salva o conteúdo
file = open(r'path\to\folder\{0:0>3}_{1:0>3}.pdf'.format(setor, quadra), 'bw')
file.write(fileobj.read())
file.close()

print(url)
