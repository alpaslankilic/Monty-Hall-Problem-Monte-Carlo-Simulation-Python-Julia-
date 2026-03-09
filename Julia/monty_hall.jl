using Random, Statistics, Plots
gr()


function simulate_monty_hall(N::Int, rng::AbstractRNG)::Tuple{Float64, Float64}
    X = rand(rng, 1:3, N)
    Y = rand(rng, 1:3, N)
    Z = ifelse.(X .== Y, mod.(X, 3) .+ 1, Y)
    return mean(X .== Y), mean(Z .== Y)
end


function run_simulation(n_values::Vector{Int}; seed::Int=42)::Tuple{Vector{Float64}, Vector{Float64}}
    rng = MersenneTwister(seed)
    p1_results = Float64[]
    p2_results = Float64[]

    for N in n_values
        p1, p2 = simulate_monty_hall(N, rng)
        push!(p1_results, p1)
        push!(p2_results, p2)
    end

    return p1_results, p2_results
end


function plot_results(n_values::Vector{Int}, p1::Vector{Float64}, p2::Vector{Float64})
    p = plot(n_values, p1,
        xscale      = :log10,
        label       = "Stick",
        color       = :orange,
        lw          = 2,
        xlabel      = "Number of Trials (N)",
        ylabel      = "Probability of Winning",
        title       = "Monty Hall — Monte Carlo Simulation",
        grid        = true,
        legend      = :right,
        size        = (800, 450),
        framestyle  = :box,
        margin      = 5Plots.mm
    )
    plot!(n_values, p2, label="Switch", color=:blue, lw=2)

    savefig(p, "monty_hall.png")
    return p
end


function main()
    n_values = unique(round.(Int, 10 .^ range(3, 6, length=60)))
    p1_results, p2_results = run_simulation(n_values)
    return plot_results(n_values, p1_results, p2_results)
end


main()
