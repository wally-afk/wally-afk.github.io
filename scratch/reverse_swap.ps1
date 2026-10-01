$content = Get-Content -Raw -Path index.html

# Fix encoding issue from previous run
$content = $content -replace '\?"', '—'

# Project 02 (currently Bikes)
$regex2 = '(?s)(<!-- PROJECT 02 — KILLER GLUTE BIKES BI  -->.*?)(?=<!-- PROJECT 03)'
if ($content -match $regex2) {
    $p2Block = $matches[1]
}

# Project 06 (currently Supermarkets)
$regex6 = '(?s)(<!-- PROJECT 06 — SMI SUPERMARKETS \(full width\) -->.*?)(?=\s*</div><!-- /projects-grid -->)'
if ($content -match $regex6) {
    $p6Block = $matches[1]
}

if ($p2Block -and $p6Block) {
    Write-Host "Found both blocks."
    
    # Process current P6 (Supermarkets) to become P2
    $newP2 = $p6Block -replace 'PROJECT 06', 'PROJECT 02'
    $newP2 = $newP2 -replace '<span class="proj-num">06</span>', '<span class="proj-num">02</span>'
    $newP2 = $newP2 -replace ' project-card--full', ''
    $newP2 = $newP2 -replace '\(full width\)', ''
    
    # Process current P2 (Bikes) to become P6
    $newP6 = $p2Block -replace 'PROJECT 02', 'PROJECT 06'
    $newP6 = $newP6 -replace '<span class="proj-num">02</span>', '<span class="proj-num">06</span>'
    $newP6 = $newP6 -replace 'class="card project-card"', 'class="card project-card project-card--full"'
    $newP6 = $newP6 -replace 'PROJECT 06 — KILLER GLUTE BIKES BI  ', 'PROJECT 06 — KILLER GLUTE BIKES BI (full width)'
    
    # We might have extra spaces, let's just make it exact:
    # "PROJECT 06 — KILLER GLUTE BIKES BI " -> "PROJECT 06 — KILLER GLUTE BIKES BI (full width)"
    $newP6 = $newP6 -replace 'BI  -->', 'BI (full width) -->'
    
    # Replace in content
    $content = $content.Replace($p2Block, "%%TEMP_P2%%")
    $content = $content.Replace($p6Block, $newP6)
    $content = $content.Replace("%%TEMP_P2%%", $newP2)
    
    Set-Content -Path index.html -Value $content -Encoding UTF8
    Write-Host "Reverse swap completed successfully."
} else {
    Write-Host "Could not find one or both blocks."
}
