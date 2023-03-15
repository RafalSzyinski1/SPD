mutable struct RandomNumberGenerator
    seed::Real
end 

function nextInt(RNG::RandomNumberGenerator,low::Int64, high::Int64)::Int64
    m = 2147483647
    a = 16807
    b = 127773
    c = 2836
    k = floor(RNG.seed / b)
    RNG.seed = a * (RNG.seed % b) - k * c
    if RNG.seed < 0
        RNG.seed = RNG.seed + m
    end
    value_0_1 = RNG.seed
    value_0_1 /= m
    low + floor(value_0_1 * (high - low + 1)) |> Int64
end

function nextFloat(RNG::RandomNumberGenerator,low::Int64, high::Int64)::Float64
    low*=100000
    high*=100000
    nextInt(RNG,low,high)/100000.0
end

