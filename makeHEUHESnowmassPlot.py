import matplotlib
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)
matplotlib.rc('axes', labelsize=18)
matplotlib.rcParams['lines.linewidth'] = 3

#matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
matplotlib.rc('font',**{'family':'serif','serif':['Palatino']})
matplotlib.rc('text', usetex=True)
legendfontsize = 13

import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
import units
import fluxes
import os
import E2_fluxes_HESnowmass as nuplot

# YOU NEED TO CHANGE THIS IN E2_fluxes_NuTauSnowmass,
# expdata.py AND modeldata.py 
# TO UPDATE PROPERLY
energyBinsPerDecade = 1.
plotUnitsEnergy = units.eV
plotUnitsEnergyStr = "eV"
plotUnitsFlux = units.GeV * units.cm ** -2 * units.second ** -1 * units.sr ** -1
flavorRatio = 1.
DIFFUSE = True
livetime = 10 * units.year
subtitles = [""]

#subtitles = ['Water and Ice', "Atmosphere, Earth's Limb, Topography", "$\nu_\tau$ Only"]
def axtrans(x, ax, bx):
    return (np.log(x) - np.log(ax))/(np.log(bx) - np.log(ax))


# identify which subplot to include
show_icecube = [0]
show_icecube_uhe = [0]
show_anita = [0]
show_pueo = [0]
show_poemma = [0]
show_eusospb =[0]
show_auger = [0]
show_ara = [0]
show_arianna = [0]
show_grand = [0]
show_beacon = [0]
show_taroge = [0]
show_trinity = [0]
show_tambo = [0]
show_radar = [0]
show_rnog = [0]
show_gen2 = [0]

fig, axs = plt.subplots(1, 1, figsize=(12, 8))
second_axs = []     
for i in range(0,1):
    nuplot.get_E2_limit_figure(fig=fig, ax=axs,show_model_legend=True,
                                      diffuse=DIFFUSE,
                                                              show_ice_cube_EHE_limit=i in show_icecube_uhe,
                                                              show_ice_cube_HESE_data=False,
                                                              show_ice_cube_HESE_fit=i in show_icecube,
                                                              show_ice_cube_mu=i in show_icecube,
                                                              nu_mu_show_data_points=False,
                                                              show_ice_cube_mu_extrap=False,
                                                              show_icecube_glashow=False,
                                                              show_anita_I_III_limit=False,
                                                                show_anita_I_IV_limit=i in show_anita,
                                                              show_pueo30=False,
                                                              show_pueo100=i in show_pueo,
                                                              show_poemma=i in show_poemma,
                                                              show_poemma360=False,
                                                              show_poemma_fluor=i in show_poemma,
                                                              show_eusospb=False,
                                                              show_auger_limit=i in show_auger,
                                                              show_ara=i in show_ara,
                                                              show_ara_2023=False,
                                                              show_ara_2023_TL=False,
                                                              show_arianna=i in show_arianna,
                                                              show_grand_10k=False,
                                                              show_grand_200k=i in show_grand,
                                                              show_beacon=i in show_beacon,
                                                              show_taroge=False,
                                                              show_tambo=i in show_tambo,
                                                              show_trinity=i in show_trinity,
                                                              show_ska=False,
                                                              show_radar=i in show_radar,
                                                              show_RNOG=i in show_rnog,
                                                              show_IceCubeGen2_whitepaper=False,
                                                              show_IceCubeGen2_ICRC2021=False,
                                                              show_IceCubeGen2_combo=i in show_gen2,
                                                              show_IceCubeGen2_proj=False,
                                                              show_ara_1year=False,
                                                              show_prediction_arianna_200=False,
                                                              show_Heinze=False,
                                                              show_Auger_vanvliet=True,
                                                              show_TA=False,
                                                              show_TA_nominal=False,
                                                              show_TA_ICRC2021=False,
                                                              show_neutrino_best_fit=False,
                                                              show_neutrino_best_case=False,
                                                              show_neutrino_worst_case=False,
                                                              show_muf_bestfit=True,
                                                              show_astro=True)
    axs.set_yscale('log')
    axs.set_xscale('log')
    axs.set_xlabel(f'Neutrino Energy [{plotUnitsEnergyStr}]', fontsize=18)  
    axs.set_ylabel(r'All Flavor $E^2\Phi$ [GeV cm$^{-2}$ s$^{-1}$ sr$^{-1}$]',fontsize=18)
    axs.set_title(subtitles[i])
    #second_axs.append(axs[i].secondary_yaxis('right', functions=(lambda x: 3. * x, lambda x: x / 3.)))
    #second_axs[i].set_ylabel(r"All Flavor $E^2\Phi$ [GeV cm$^{-2}$ s$^{-1}$ sr$^{-1}]$", fontsize=12)
    axs.grid(True, which='minor', alpha=0.1)
    axs.grid(True, which='major', alpha=0.4)
    #axs[i].legend(loc='lower left', fontsize=12)
    
    
    minx = 1.2e13 * units.eV / plotUnitsEnergy
    maxx = 1e21 * units.eV / plotUnitsEnergy
    miny= 0.2e-10*3
    maxy =  1e-5*3
    # transformed coordinates for arrow from (1E-10,1E-18) to (1E-4,1E-16)
    x0 = axtrans(1.6e15, ax=minx, bx=maxx)
    y0 = axtrans(1e-6, ax=miny, bx=maxy)
    x1 = 0
    y1 = axtrans(0.8e-9, ax=miny, bx=maxy) - axtrans(1e-6, ax=miny, bx=maxy)
    axs.arrow( x0, y0, x1, y1, # input transformed arrow coordinates 
               transform = axs.transAxes, # tell matplotlib to use axes coordinates   
               linewidth=8, alpha=0.4)
               
    axs.annotate("Coming\ndecades", (0.8e15, 1.1e-9), fontsize=12, alpha=0.9, rotation=90)
    axs.annotate("Near term", (1.1e15, 5e-8), fontsize=12,alpha=0.9, rotation=90)
    axs.annotate("Now", (1.1e15, 0.6e-6), fontsize=12,alpha=0.9, rotation=90)
    
    #axs.plot(3e15,1e-6, 'ko', marker=r'$\downarrow$', markersize=20)
    if DIFFUSE:
        
        axs.set_ylim(miny,maxy)
        axs.set_xlim(minx,maxx)
        #axs[i].set_yticks([1e-12, 1e-11,1e-10,1e-9,1e-8,1e-7, 1e-6, 1e-5])
        axs.set_yticks([1e-10,1e-9,1e-8,1e-7, 1e-6, 1e-5])
        axs.yaxis.set_minor_locator(tck.AutoMinorLocator())
        axs.minorticks_on()
        #axs[i].tick_params(axis='y', which='minor', left=True)
    
        

fig.suptitle("Diffuse Flux, 1:1:1 Flavor Ratio  ", fontsize=18)
fig.subplots_adjust(top=0.94, hspace=0.18, bottom=0.09, right=0.92, left=0.08)
#fig.tight_layout()
#labels = []
#labels = add_limit(ax, labels, veff[:, 0], veff[:, 1], n_stations=100, livetime=5 * units.year, label=veff_label)
#labels = add_limit(ax, labels, veff[:, 0], veff[:, 1], n_stations=1000, livetime=5 * units.year, label=veff_label)
#plt.legend(handles=labels, loc=2)
if DIFFUSE:
    name_plot = "Limit_diffuse_single.pdf"
else:
    name_plot = "Limit_sources.pdf"
plt.savefig(name_plot)
plt.show()