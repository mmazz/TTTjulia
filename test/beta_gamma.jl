include("../src/TrueSkill.jl")
using .TrueSkill
global const ttt = TrueSkill
using Test
using CSV
using JLD2
using Dates
using DataFrames
using LinearAlgebra

data = CSV.read("./KGS_filtered_julia.csv")
data = data[1:300000,:]

prior_dict = Dict{String,ttt.Rating}()
for h_key in Set([(row.handicap, row.width) for row in eachrow(data) ])
    prior_dict[string(h_key)] = ttt.Rating(0.,25.0/3.,0.,1.0/100)
end
results = [row.black_win == 1 ? [1,0] : [0, 1] for row in eachrow(data) ]
composition = [ r.handicap<2 ? [[string(r.white)],[string(r.black)]] : [[string(r.white)],[string(r.black),string((r.handicap,r.width))]] for r in eachrow(data) ]

betas = [25.0,25/2,25/4,25/5,25/6]
#betas = [25.0,25/2,25/4,25/5,25/6,25/8,25/10,25/12]

#gammas = [0.25,0.75,1.25,2.0,4.0,7.0,10.0,30.0]
gammas = [7.0,10.0,30.0]

matrix_ev = zeros(Float64, length(betas), length(gammas)) # filas columnas


for i in 1:length(betas)
    for j in 1:length(gammas)

        times = Vector{Int64}()
        ttt.setbeta(betas[i])
        ttt.setgamma(gammas[j])

        h = ttt.History(composition, results, times , prior_dict)
        ttt.convergence(h)

        evidence = [ h.batches[r].evidences[1] for r in 1:size(data)[1]]
        logevidence = log.(evidence)
        prom_log_ev = -1*sum(logevidence)/length(evidence)
        matrix_ev[i,j] = prom_log_ev
    end
end

println(matrix_ev)
df = DataFrame(matrix_ev)
DataFrames.rename!(df, [Symbol("Gamma=$i") for i in gammas])
insert!(df, 1, betas, :betas)
CSV.write("matrix_ev_gammas_grandes2.csv",  df, writeheader=true)
