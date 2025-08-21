def si_no(prompt):
    """Pregunta al usuario y normaliza respuestas sí/no (s/n)."""
    while True:
        r = input(prompt + " [s/n]: ").strip().lower()
        if r in ("s", "si", "sí", "y"):
            return True
        if r in ("n", "no"):
            return False
        print("Por favor responde con 's' o 'n'.")

def diagnosticar():
    print("="*70)
    print("   SISTEMA EXPERTO: DIAGNÓSTICO RÁPIDO DE FALLAS EN AUTOMÓVILES")
    print("="*70)
    print("Responde a unas preguntas breves y te sugeriré posibles causas.")
    print()

    arranca = si_no("¿El auto ARRANCA?")
    luces_tablero = None
    if not arranca:
        luces_tablero = si_no("¿Las luces del tablero ENCIENDEN al girar la llave?")
    se_apaga_al_acelerar = si_no("¿El auto se apaga cuando ACELERAS?")
    humo_negro = si_no("¿Sale HUMO NEGRO por el escape?")
    humo_blanco_constante = si_no("¿Sale HUMO BLANCO CONSTANTE por el escape?")

    posibles_causas = []

    if (arranca is False) and (luces_tablero is False):
        posibles_causas.append("Batería descargada o conexiones de batería defectuosas.")

    if (arranca is False) and (luces_tablero is True):
        posibles_causas.append("Falla en el motor de arranque (arrancador/solenoide/relé).")

    if (arranca is True) and se_apaga_al_acelerar:
        posibles_causas.append("Problema en el suministro de combustible (bomba/filtro/inyectores).")

    if humo_negro:
        posibles_causas.append("Mezcla rica de combustible (sensor MAF/O2, inyector goteando, presión alta).")

    if humo_blanco_constante:
        posibles_causas.append("Posible falla en la junta de culata (antigel en cámara de combustión).")

    print("\n— RESULTADO —")
    if posibles_causas:
        vistas = set()
        deducidas = [c for c in posibles_causas if not (c in vistas or vistas.add(c))]
        for i, causa in enumerate(deducidas, 1):
            print(f"{i}. {causa}")
    else:
        print("No se pudo determinar una causa con las reglas actuales.")
        print("Revisa otros síntomas (testigo Check Engine, ruidos, fugas) o consulta a un especialista.")

    print("\nConsejo: estas son sugerencias iniciales. Verifica con pruebas básicas:")
    print(" - Batería: voltaje en reposo (~12.6V) y al arrancar (>10V).")
    print(" - Combustible: presión de riel según especificación; filtro en buen estado.")
    print(" - Escáner OBD-II: lee códigos de falla para orientar el diagnóstico.")
    print("\nGracias por usar el sistema experto.\n")

def main():
    while True:
        diagnosticar()
        if not si_no("¿Deseas realizar otro diagnóstico?"):
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
