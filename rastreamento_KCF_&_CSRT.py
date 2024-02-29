import cv2

# escolha o rastreador
#rastreador = cv2.TrackerKCF_create() #chama o rastreador KCK
rastreador = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('race.mp4')
ok, frame = video.read() #fazer a leitura do primeiro frame do video 
#variavel ok eh para retornar True ou False para a leitura do video, 

bbox = cv2.selectROI(frame) #ROI = region of interest / bounding box
#print(bbox) #print as coordenadas (l,t,w,h)

ok = rastreador.init(frame,bbox)
#print(ok) 

#tudo acima executa apenas no primeiro frame
#o while abaixo eh para executar no video todo

while True:
    ok, frame = video.read()
    #print(ok) Ver se o video esta sendo rodado corretamente

    if not ok: #quando o video acabar ok sera False e executa o break
        break

    ok, bbox = rastreador.update(frame) #atualizacao do bounding box
    #print(bbox) #acompanhamento da atualizacao do bbox

    if ok:
        (x,y,w,h) = [int(v) for v in bbox] #percorre dentro dos valores do bbox
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2,1)
    else:
        cv2.putText(frame,'Erro',(100,80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255),2)

    cv2.imshow('Rastreamento',frame)
    if cv2.waitKey(1) & 0XFF == 27: #apertar a tecla esc para parar o codigo
        break