using Random
using Plots

function simulate_monty_hall(N::Int, rng::AbstractRNG)::Tuple{Float64, Float64}
    initial_choice = rand(rng, 1:3, N)
    prize = rand(rng, 1:3, N)

    switch_choice = ifelse.(initial_choice .== prize, mod.(initial_choice, 3) .+ 1, prize)

    p_stick = mean(initial_choice .== prize)
    p_switch = mean(switch_choice .== prize)

    return p_stick, p_switch
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
    plot(n_values, p1,
        xscale=:log10,
        label="Stick",
        color=:orange,
        lw=1.5,
        xlabel="Number of Trials (N)",
        ylabel="Probability of Winning",
        title="Monty Hall Monte Carlo Simulation",
        grid=true
    )
    plot!(n_values, p2, label="Switch", color=:blue, lw=1.5)
    hline!([1/3], color=:orange, ls=:dash, lw=0.8, label="Theory 1/3")
    hline!([2/3], color=:blue, ls=:dash, lw=0.8, label="Theory 2/3")

    savefig("monty_hall.png")
end

function main()
    n_values = unique(round.(Int, 10 .^ range(3, 6, length=60)))
    p1_results, p2_results = run_simulation(n_values)
    plot_results(n_values, p1_results, p2_results)
end

main()
