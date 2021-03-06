import random
import numpy as np

from genMD.shapes.np_base import NPBase
from genMD.augmenters.dna import *
import genMD.bonds
import genMD.utils.points as points

        
class NPDiamond(NPBase):
    def make_shape(self):
        r= self.x_length
        r = float(r)
        a=r/2.
        b = self.pheight
        #center point
        self.ssDNA.append([a,a,r/4,{'name':self.Ntype,'type':self.body_type}])
        #base of pyramid
        #self.make_side([0,r,0],[r,r,0],[0,0,0],[r,0,0],num=1)
        #sides of pyramid
        #self.make_side([0,0,0],[r/2,r/2,r/b],[r,0,0],[r/2,r/2,r/b],num=2)
        #self.make_side([0,0,0],[r/2,r/2,r/b],[0,r,0],[r/2,r/2,r/b],num=3)
        #self.make_side([r,r,0],[r/2,r/2,r/b],[r,0,0],[r/2,r/2,r/b],num=4)
        #self.make_side([r,r,0],[r/2,r/2,r/b],[0,r,0],[r/2,r/2,r/b],num=5)
        self.make_side([0,0,0],[r/2,r/2,r/b],[0,0,0],[r,0,0],num=2,t=3)
        self.make_side([0,0,0],[r/2,r/2,r/b],[0,0,0],[0,r,0],num=2,t=3)
        self.make_side([r,r,0],[r/2,r/2,r/b],[r,r,0],[r,0,0],num=2,t=3)
        self.make_side([r,r,0],[r/2,r/2,r/b],[r,r,0],[0,r,0],num=2,t=3)
        self.make_side([0,0,0],[r/2,r/2,-r/b],[0,0,0],[r,0,0],num=2,t=3)
        self.make_side([0,0,0],[r/2,r/2,-r/b],[0,0,0],[0,r,0],num=2,t=3)
        self.make_side([r,r,0],[r/2,r/2,-r/b],[r,r,0],[r,0,0],num=2,t=3)
        self.make_side([r,r,0],[r/2,r/2,-r/b],[r,r,0],[0,r,0],num=2,t=3)
    def add_dna(self):
        for i,j in enumerate(self.bond_MN):
            self.L=[]
            self.N=[]
            self.S=[]
            pt =  self.ssDNA[self.bond_MN[i]]
            self.vx, self.vy, self.vz = points.unit_vect(pt[0],pt[1],pt[2],self.x_length/2.0, self.x_length/2.0,
                    self.x_length/2.0)
            self.vx=self.vx/self.scale
            self.vy=self.vy/self.scale
            self.vz=self.vz/self.scale
            if self.make_rigid:
                spacer_ds(self,self.ssDNA[self.bond_MN[i]][0],self.ssDNA[self.bond_MN[i]][1],self.ssDNA[self.bond_MN[i]][2],i)
            else:
                spacer(self,self.ssDNA[self.bond_MN[i]][0],self.ssDNA[self.bond_MN[i]][1],self.ssDNA[self.bond_MN[i]][2],i)
            if self.no_linker == False:
                linker(self,j)
                nucleotide(self,j)
            else:
                end_bead(self,j)
    #Actually make the dna ie grow it 
    def grow(self):
        #Find the coordinates of the Nanoparticle 22beads
        self.make_shape()
        #Find the bonds to attatch the ssDNA to the Nanoparticle
        self.bond_MN =[]
        num_dna = len(self.ssDNA)/4
        bonds.add_bonds_side(self.bond_MN,self.side,min_side=10,num_dna=num_dna)
        #Add dna to the Nanoparticle
        self.data['num_dna'] = len(self.bond_MN)
        self.add_dna()

        