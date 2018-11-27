# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import base_de_datos as bd
from solicitud import Solicitud
from vehiculo import Vehiculo
from repuesto import Repuesto
from datetime import timedelta, datetime
import gestionador
from functools import reduce


class VistaSolicitudAgregada(PanedWindow):
    """Panel que contiene los campos para introducir los datos de la solicitud"""

    cliente_entry = None
    asesor_entry = None
    tipo_entry = None
    marcaR_entry = None
    costo_entry = None
    marcaV_entry = None
    modelo_entry = None
    chapa_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        """Inicializamos la ventana de creacion de solicitudes con los respectivos inputs"""
        Label(self, text="Ingrese datos de la solicitud", ).grid(
            row=1, column=2)
        Label(self, text="Cliente*: ").grid(row=2, column=1)
        Label(self, text="Asesor*: ").grid(row=3, column=1)
        Label(self, text="Vehiculo*: ").grid(row=4, column=1)
        Label(self, text="Chapa*: ").grid(row=5, column=2)
        Label(self, text="Marca*: ").grid(row=6, column=2)
        Label(self, text="Modelo*: ").grid(row=7, column=2)
        Label(self, text="Repuesto: ").grid(row=9, column=1)
        Label(self, text="Tipo: ").grid(row=10, column=2)
        Label(self, text="Marca: ").grid(row=11, column=2)
        Label(self, text="Costo: ").grid(row=12, column=2)
        Button(self, text="GUARDAR", command=self.agregar_solicitud).grid(
            row=14, column=1)

        self.get_cliente_entry()
        self.get_asesor_entry()
        self.get_chapa_entry()
        self.get_marcaV_entry()
        self.get_modelo_entry()
        self.get_tipo_entry()
        self.get_marcaR_entry()
        self.get_costo_entry()

    def get_cliente_entry(self):
        if not self.cliente_entry:
            self.cliente_entry = Entry(master=self, width=20)
            self.cliente_entry.grid(row=2, column=2)
        return self.cliente_entry

    def get_asesor_entry(self):
        if not self.asesor_entry:
            self.asesor_entry = Entry(master=self, width=20)
            self.asesor_entry.grid(row=3, column=2)
        return self.asesor_entry

    def get_chapa_entry(self):
        if not self.chapa_entry:
            self.chapa_entry = Entry(master=self, width=20)
            self.chapa_entry.grid(row=5, column=3)
        return self.chapa_entry

    def get_marcaV_entry(self):
        if not self.marcaV_entry:
            self.marcaV_entry = Entry(master=self, width=20)
            self.marcaV_entry.grid(row=6, column=3)
        return self.marcaV_entry

    def get_modelo_entry(self):
        if not self.modelo_entry:
            self.modelo_entry = Entry(master=self, width=20)
            self.modelo_entry.grid(row=7, column=3)
        return self.modelo_entry

    def get_tipo_entry(self):
        if not self.tipo_entry:
            self.tipo_entry = Entry(master=self, width=20)
            self.tipo_entry.grid(row=10, column=3)
        return self.tipo_entry

    def get_marcaR_entry(self):
        if not self.marcaR_entry:
            self.marcaR_entry = Entry(master=self, width=20)
            self.marcaR_entry.grid(row=11, column=3)
        return self.marcaR_entry

    def get_costo_entry(self):
        if not self.costo_entry:
            self.costo_entry = Entry(master=self, width=20)
            self.costo_entry.grid(row=12, column=3)
        return self.costo_entry

    def validar_solicitud(self, cliente, asesor):
        """Validamos que la solicitud ingresada sea correcta"""
        val = False
        if cliente.isdigit() and asesor.isdigit():
            val = True
        else:
            messagebox.showinfo("", "Ingrese cedula del cliente y asesor")
        return val

    def agregar_solicitud(self):
        """Funcion para agregar una solicitud a base de datos"""
        try:
            cli = self.get_cliente_entry().get()
            asesor = self.get_asesor_entry().get()
            mod = self.get_modelo_entry().get()
            mar = self.get_marcaV_entry().get()
            cha = self.get_chapa_entry().get()
            tip = self.get_tipo_entry().get()
            marcaR = self.get_marcaR_entry().get()
            cos = self.get_costo_entry().get()
            if self.validar_solicitud(cli, asesor):
                if self.validar_vehiculo(mod, mar, cha):
                    vehiculo = Vehiculo(**{"modelo": mod, "marca": mar, "chapa": cha})
                else:
                    messagebox.showinfo("Informacion", "Debe ingresar los datos del vehiculo correctamente")
                if self.validar_repuesto(tip, marcaR, cos):
                    repuesto = Repuesto(**{"tipo": tip, "marca": marcaR, "costo": cos})
                else:
                    messagebox.showinfo("Informacion", "Debe ingresar los datos de repuestos correctamente")
                solicitud = Solicitud(**{"fecha": datetime.now(),
                                         "cliente": cli, "asesor": asesor, "vehiculo": vehiculo, "repuestos": repuesto})
                bd.solicitudes.append(solicitud)
                messagebox.showinfo("Informacion", "Solicitud agregada")
                gestionador.guardar_datos()
                self.destroy()
        except Exception as e:
            messagebox.showerror('Error', e)

    def validar_repuesto(self, tip, mar, cos):
        """Validamos que el repuesto sea correcto"""
        val = False
        if tip != "" and mar != "" and (cos.isdigit() or cos == ""):
            val = True
        elif tip == "" and mar == "" and cos == "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del " +
                                "repuesto")
        return val

    def validar_vehiculo(self, mod, mar, cha):
        """Validamos que el vehiculo ingresado sea correcto"""
        val = False
        if mar != "" and mod != "" and cha != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del " +
                                "vehiculo")
        return val


class VistaSoliBaja(PanedWindow):
    """Panel que contien los campos para procesar una solicitud"""
    soli_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        Label(self, text="Ingrese datos requeridos", ).grid(row=1, column=2)
        Label(self, text="Ingrese numero de solicitud a procesar*: ").grid(
            row=2, column=1)
        Button(self, text="Procesar", command=self.procesar).grid(
            row=3, column=1)

        self.get_soli_entry()

    def get_soli_entry(self):
        if not self.soli_entry:
            self.soli_entry = Entry(master=self, width=20)
            self.soli_entry.grid(row=2, column=2)
        return self.soli_entry

    def procesar(self):
        """Esta funcion da de baja una solicitud, almacena la solicitud en la lista de solicitudes_baja
        imprime en pantalla los datos del mantenimiento"""
        try:
            pos = int(self.get_soli_entry().get())
            if (messagebox.askyesno("Procesar", "Desea atender la solicitud?")):
                dato = bd.solicitudes.pop(pos - 1)
                bd.solicitudes_baja.append(dato)
                gestionador.guardar_datos()
                messagebox.showinfo("Informacion", "Solicitud Atendida")
                self.calc(dato)
        except:
            messagebox.showerror("Infor", "No existe solicitud")

    def calc(self, dato):
        """Funcion que calcula los valores para procesar una solicitud"""
        monto = self.generador(dato)
        messagebox.showinfo("Resultado", "Cliente: " + dato.cliente +
                            "\Asesor: " + dato.asesor + "\nMonto total: " + str(monto))
        self.destroy()

    def generador(self, dato):
        """ Se retorna el costo final del mantenimiento """
        costo_general = 100000
        if dato.vehiculo:
            if dato.repuestos:
                costo_general += int(dato.repuestos.costo)
        return costo_general