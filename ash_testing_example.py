# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:09:50 2015

@author: bcolsen
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats

from ash import ash

plt.rcParams['svg.fonttype'] = 'none'

# %% Make Fake data and store it in excell.
# Don't do this if you have real data

mu, sigma = 6.35, 0.13
data_fake_a = mu + sigma*np.random.randn(50)

mu2, sigma2 = 6.5, 0.10
data_fake_b = mu2 + sigma2*np.random.randn(50)

df_fake = pd.DataFrame({'fake_a':data_fake_a, 'fake_b':data_fake_b})
df_fake.to_excel('fake_data.xlsx')


# %% Import tha data and assign a and b

filename = 'fake_data.xlsx' #Change this

df = pd.read_excel('fake_data.xlsx')

a = df['fake_a']
b = df['fake_b']

label_a = "Fake A"
label_b = "Fake B"

xlabel = 'Fakeness (%)'

fig = plt.figure(num = 'ASH Plot testing', figsize = (4,4))
fig.clf()


ash_obj_a = ash(a)
ash_obj_b = ash(b)

ax = plt.subplot()

#plot ASH as a line
ax.plot(ash_obj_b.ash_mesh,ash_obj_b.ash_den,lw=2, color = '#D95319')
ax.plot(ash_obj_a.ash_mesh,ash_obj_a.ash_den,lw=2, color = '#365994')


#plot the solid ASH
ash_obj_b.plot_ash_infill(ax, color ='#F2966E')
ash_obj_a.plot_ash_infill(ax, color='#92B2E7')


#plot KDE
ax.plot(ash_obj_a.kde_mesh,ash_obj_a.kde_den,lw=1, color ='#365994')
ax.plot(ash_obj_b.kde_mesh,ash_obj_b.kde_den,lw=1, color = '#D95319')

# Make a Rugplot (the barcode like data representation)
ash_obj_a.plot_rug(ax, alpha=1, color = '#4C72B0', ms = 8, height = 0.10)
ash_obj_b.plot_rug(ax, alpha=1, color ='#F2966E', ms = 8, height = 0.04)

if ash_obj_a.mean <= ash_obj_b.mean:
    ash_obj_a.plot_stats(ax, label_a, color = '#365994')
    ash_obj_b.plot_stats(ax, label_b, side='right', color ='#D95319')
else:
    ash_obj_a.plot_stats(ax, label_a, side='right', color = '#365994')
    ash_obj_b.plot_stats(ax, label_b, color ='#D95319')

# add a line showing the expected distribution
dista = stats.norm.pdf(ash_obj_a.ash_mesh, mu, sigma)
plt.plot(ash_obj_a.ash_mesh,dista,'b--',lw=2)
plt.plot(ash_obj_a.ash_mesh,dista-ash_obj_a.ash_den,'b--',lw=1)

distb = stats.norm.pdf(ash_obj_b.ash_mesh, mu2, sigma2)
plt.plot(ash_obj_b.ash_mesh,distb,'r--',lw=2)
plt.plot(ash_obj_b.ash_mesh,distb-ash_obj_b.ash_den,'r--',lw=1)

ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(direction='out')
ax.set_yticks([])

print(label_a, ash_obj_a.mean, ash_obj_a.sigma)
ad_stat, ad_crit, ad_signi = stats.anderson_ksamp((a,b))
print('ad',label_a, ad_stat, ad_crit, ad_signi)
ks_stat, ks_signi = stats.ks_2samp(a,b)
print('ks',label_a, ks_stat, ks_signi)
print(ash_obj_a.bw, ash_obj_a.bin_num, ash_obj_a.bin_width, ash_obj_a.bin_edges[1]-ash_obj_a.bin_edges[0])
print(ash_obj_b.bw, ash_obj_b.bin_num, ash_obj_b.bin_width, ash_obj_b.bin_edges[1]-ash_obj_b.bin_edges[0])
ad_ks_str = "p = {:.2f} %".format(ad_signi*100, ks_signi*100)
#p value text
ax.text(0.05, 0.75, ad_ks_str, color='k', ha='left', va='center', transform=ax.transAxes, size=14)
plt.xlabel(xlabel)
    

plt.tight_layout()
plt.subplots_adjust(top=0.95)
fig.text(0.47, 0.97, label_a, size=14, color='#365994', ha='right')
fig.text(0.5, 0.97, 'vs.', size=14, ha='center')
fig.text(0.53, 0.97, label_b, size=14, color='#D95319', ha='left')

fig.savefig(label_a + '_vs_' + label_b + 'testing.svg', dpi=300, transparent=True)


plt.show()
