class GeneratorU:
    def export_u(self, speed):
        export = """/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\\\    /   O peration     | Website:  https://openfoam.org
    \\\\  /    A nd           | Version:  11
     \\\\/     M anipulation  |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    format      ascii;
    class       volVectorField;
    location    "0";
    object      U;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 1 -1 0 0 0 0];

internalField   uniform (0 0 0);

boundaryField
{
inlet
{
    type            fixedValue;
    value           uniform (""" f"{speed}" """ 0 0);
}
outlet
{
    type            zeroGradient;
}
wall
{
    type            fixedValue;
    value           uniform (0 0 0);
}
cylinder_1
{
    type            fixedValue;
    value           uniform (0 0 0);
}
cylinder_2
{
    type            fixedValue;
    value           uniform (0 0 0);
}
cylinder_3
{
    type            fixedValue;
    value           uniform (0 0 0);
}
frontAndBack
{
    type            empty;
}
}


// ************************************************************************* //
"""

        with open("0/U", "w") as file:
            file.write(export)
