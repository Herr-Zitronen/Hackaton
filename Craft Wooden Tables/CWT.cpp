#include <iostream>
using namespace std;

typedef long long ll;

bool se_pueden_construir(ll mesas_a_probar, ll madera_por_mesa, ll espacios_totales, ll max_madera_por_pila, ll madera_total) {
    if (mesas_a_probar * madera_por_mesa > madera_total) return false;

    ll madera_restante = madera_total - mesas_a_probar * madera_por_mesa;
    ll espacios_ocupados = (madera_restante + max_madera_por_pila - 1) / max_madera_por_pila;
    ll espacios_libres = espacios_totales - espacios_ocupados;
    return espacios_libres >= mesas_a_probar;
}

int main() {
    ll madera_por_mesa, espacios_totales, max_madera_por_pila, madera_total;
    cin >> madera_por_mesa >> espacios_totales >> max_madera_por_pila >> madera_total;

    ll inferior = 0;
    ll superior = madera_total / madera_por_mesa;
    ll respuesta_final = 0;

    while (inferior <= superior) {
        ll medio = (inferior + superior) / 2;
        if (se_pueden_construir(medio, madera_por_mesa, espacios_totales, max_madera_por_pila, madera_total)) {
            respuesta_final = medio;
            inferior = medio + 1;
        } else {
            superior = medio - 1;
        }
    }

    cout << respuesta_final << endl;
    return 0;
}
