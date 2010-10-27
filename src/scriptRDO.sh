cd ../../jm-normal/
git checkout master
cd lencod/
make
cd ../../jm-heuristic/
git checkout master
cd lencod/
make
cd ../../GeraResultados/src/
python geraResultados.py

