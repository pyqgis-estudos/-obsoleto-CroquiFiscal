import urllib, os

# Diretório
folder_dir = r'path\to\folder\CADASTRO Croqui_Fiscal'
if # se não existe o dir:
  os.makedirs(folder_dir)

# Definição do SQ
setor = 299
quadra = 47

# SQ dado
SQ_Lista = [[setor, quadra],]
# Lista de SQ
SQ_Lista = [[,],[,],[,]]
# SQ das feições selecionadas
SQ_Lista = []
for feat in features:
  setor = 
  quadra = 
  SQ_Lista.append([setor, quadra])
  

# Loop para cada SQ
for SQ in SQ_Lista:
  # Requerimento ao endereço da prodam
  uri_prodam = 'http://sf9402.app.prodam/intranet/frmConsultaCroquiPDF.aspx?pstrSetor={0:0>3}&pstrQuadra={1:0>3}'.format(SQ[0], SQ[1])
  uri_pub = 'http://geosampa.prefeitura.sp.gov.br/PaginasPublicas/DownloadCroqui.aspx?setor={0:0>3}&quadra={1:0>3}'.format(SQ[0], SQ[1])
  fileobj = urllib.request.urlopen (uri_pub)

  # print(url)  # Verificação da uri

  # Cria um novo arquivo e salva o conteúdo
  ##TODO: Criar diretório
  file = open(r'path\to\folder\CADASTRO Croqui_Fiscal\CF {0:0>3}_{1:0>3}.pdf'.format(SQ[0], SQ[1]), 'bw')
  file.write(fileobj.read())
  file.close()
