import urllib

# Definição do SQ
setor = 299
quadra = 47

# Requerimento ao endereço da prodam
uri_prodam = 'http://sf9402.app.prodam/intranet/frmConsultaCroquiPDF.aspx?pstrSetor={0:0>3}&pstrQuadra={1:0>3}'.format(setor, quadra)
uri_pub = 'http://geosampa.prefeitura.sp.gov.br/PaginasPublicas/DownloadCroqui.aspx?setor={0:0>3}&quadra={1:0>3}.format(setor, quadra)
fileobj = urllib.request.urlopen (uri_pub)

# print(url)

# Cria um novo arquivo e salva o conteúdo
file = open(r'path\to\folder\CADASTRO Croqui_Fiscal\CF {0:0>3}_{1:0>3}.pdf'.format(setor, quadra), 'bw')
file.write(fileobj.read())
file.close()
