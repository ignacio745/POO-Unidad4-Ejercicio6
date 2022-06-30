from RepositorioProvincias import RepositorioProvincias
from Controlador import ControladorProvincias
from VistaPrincipal import VistaPrincipal
from ObjectEncoder import ObjectEncoder


def main():
    conn = ObjectEncoder("provincias.json")
    repo = RepositorioProvincias(conn)
    vista = VistaPrincipal()
    ctrl = ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()