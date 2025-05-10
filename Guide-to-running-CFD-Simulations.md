# Guide to running CFD Simulations

- Commercial Software 
- Open Source Software
  
## Ansys

### Supersonic Fluid Flow
Essential Quality Checks for Supersonic Wedge Flow Simulations
Beyond merely monitoring residuals, here are critical quality checks to ensure your supersonic wedge flow simulation is physically accurate:

Physical Flow Verification
Oblique Shock Angle: Compare with theoretical value (≈21.5° for your Mach 2.5, 10° wedge case)

Static/Total Pressure Ratios: Verify pressure jumps match oblique shock theory (P₀₂/P₀₁ ≈ 0.918)

Mach Number Change: Check post-shock Mach reduction matches theoretical predictions

Solution Quality Indicators
Monitor Points: Place several upstream and downstream of the shock to track convergence of key flow variables

Mass Conservation: Check mass flow rate at inlet vs. outlet (should be within 0.1%)

Y+ Values: Ensure proper wall resolution (Y+ < 1 for viscous sublayer resolution or 30-300 for wall functions)

Visual Inspections
Shock Structure: Confirm clean, well-defined oblique shock (not smeared across many cells)

Contour Plots: Examine pressure, temperature, Mach number, and total pressure contours for discontinuities at the shock location

Flow Uniformity: Verify uniform flow fields upstream and downstream of the shock

Boundary Layer Development: Check growth along the flat plate (especially for isothermal wall condition)

Advanced Numerical Checks
Grid Sensitivity Study: Run simulations on at least three mesh densities to ensure solution independence

CFL Stability: For density-based solvers, check if CFL number is appropriate (typically 0.5-2)

Local Shock Resolution: Ensure 10+ cells across the shock thickness

Backflow Percentage: Check outlet for reverse flow (should be <1% or zero for supersonic exit)

Solver-Specific Verification
Area-Weighted vs. Mass-Weighted Averages: Compare both average types for total pressure at outlet

Third-Order MUSCL Scheme: Verify higher-order discretization is active for accurate shock capturing

Turbulence Model Performance: Verify your turbulence model (k-ω SST recommended for adverse pressure gradients)

Comparison to Theory
Use NASA/Online Shock Calculators: Compare simulation results with theoretical oblique shock relations

Validate Total Pressure Loss Ratio: Should match theory (≈0.918 for your case)

Recommended Workflow
First check residual convergence (3-4 orders of magnitude)

Then check mass, momentum, and energy conservation

Compare shock angle and pressure jump with theory

Perform visual inspection of flow field contours

Verify boundary layer development if studying viscous effects

These comprehensive checks will ensure your simulation properly captures the physics of supersonic flow over a wedge.

what back pressure condition should i give, temperature and pressure, freestream/inlet ones?
what back pressure condition should i give, temperature and pressure, freestream/inlet ones?

Search

Images

Videos

Sources
21
image.jpg
Back Pressure Settings for Supersonic Wedge Flow
Based on the details of your supersonic wedge simulation, here's how you should configure your outlet boundary conditions:

Pressure Settings
Gauge Pressure: Set to a value lower than freestream static pressure (e.g., 0.8-0.9× freestream pressure)

For Mach 2.5 flow with 0.5 bar freestream, a reasonable value would be approximately 0.4-0.45 bar

Temperature Settings
Backflow Total Temperature: Set to match the freestream total temperature (1600K in your case)

This ensures thermodynamic consistency if any reverse flow occurs during solution initialization

Why These Values Work
For supersonic outlets, "the specified pressure will no longer be used; pressure will be extrapolated from the flow in the interior"

The boundary conditions are essentially ignored once the flow becomes supersonic at that location

Setting a lower pressure ensures the flow remains supersonic at the outlet during initial iterations

Important Notes
The back pressure only affects the solution when:

The flow is locally subsonic at the outlet

During initialization and early convergence stages

Setting too high a backflow pressure can cause problems:

"If you set a high enough backflow pressure, the outlet becomes an inlet!"

This would invalidate your simulation

For supersonic outlets, ANSYS Fluent will automatically:

Extrapolate all flow values from the interior

Disregard your specified boundary values once fully converged

For most reliable results, ensure your mesh extends far enough downstream that the flow is fully developed before reaching the outlet boundary.

on ur suggestion of extending the domain , u mean insrease the bottom flat plate isothermal wall length?
on ur suggestion of extending the domain , u mean insrease the bottom flat plate isothermal wall length?

Search

Images

Sources
35
image.jpg
Based on the image of your supersonic wedge simulation domain, I recommend extending the entire computational domain in the streamwise direction (to the right), which would include increasing the length of the bottom isothermal flat plate. Here's why:

Overall Domain Extension:

You need to extend the entire right side (red outlet boundary) further downstream

This naturally includes extending the bottom isothermal wall to match

The top boundary should also be extended correspondingly

Best Practice Guidelines:

For downstream extensions, CFD best practices recommend "minimum 5 times the dimension of the body along the direction of the flow"

This allows the wake and flow structures to fully develop before reaching the outlet

Specific Benefits:

Prevents outlet boundary conditions from influencing the flow near the wedge

Gives sufficient space for the oblique shock to fully develop

Reduces reverse flow issues at the current outlet location

Boundary Condition Handling:

With sufficient downstream extension, "an extrapolation boundary condition is appropriate" for supersonic outflow

This approach ensures the flow can properly develop without artificial constraints

The isothermal wall condition on the bottom surface should be maintained along the entire extended length to ensure consistent boundary treatment.

Related
How does extending the domain length affect the accuracy of the simulation
What are the benefits of increasing the length of the bottom flat plate
How does the domain size influence the formation of shockwaves
What are the best practices for determining the optimal domain size
How can I visualize the impact of domain extension on the flow field
