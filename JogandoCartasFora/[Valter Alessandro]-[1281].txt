while True:
   n = int(input())
   if n == 0:
    break
        
   baralho = list(range(1, n + 1))
   descarte = []

   while len(baralho) > 1:
        
        carta_topo = baralho.pop(0)
        descarte.append(carta_topo)
        
        carta_proxima = baralho.pop(0)
        baralho.append(carta_proxima)
      
   descarte, carta_restante = descarte, baralho[0]
        
   descarte_str = ', '.join(map(str, descarte))
   print(f"Discarded cards: {descarte_str}")
   print(f"Remaining card: {carta_restante}")
