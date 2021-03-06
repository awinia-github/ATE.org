# Spyder thoughts

## Conda application environment vs Spyder Installer

What if we would 'cast' Spyder into it's own conda environment (maybe called `_spyder_` ?) 

<ins>**Advantages:**</ins>
  * Even though support in `spyder` for `Python2` is dropped, the users can still develop in `Python2` ! 
  * Even more, `spyder` could follow the latest stable `Python3`, and users can use whatever 😋
  * We are no longer forced to follow the packages of anaconda (or even conda-forge for that matter) 🥳
  * Testing will become much more easy, as we need to test against the `_spyder_` environment ONLY 😌
  * We still can use conda to install plugins **to** spyder (and the plugins to these plugins 😎

<ins>**Disadvantages:**</ins> Changes are needed
  * Spyder needs to spawn the spyder-kernels in another environment like :
  ```sh     
  /usr/bin/env conda run -n anaconda spyder-kernels
  ```
  * Spyder launch script needs to change to something like :
  ```sh
  /usr/bin/env conda run -n _spyder_ spyder
  ```
  * Spyder install script needs to create the _spyder_ environment like:
  ```
  /usr/bin/env conda create -f _spyder_.yml
  ```
  Where the _spyder_.yml contains the (base) `spyder` environment dictated by `spyder`
